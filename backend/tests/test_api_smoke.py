import asyncio

import httpx

from app.database import get_db
from app.main import app
from app.routes import agent as agent_routes


def request(method, url, **kwargs):
    async def send_request():
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.request(method, url, **kwargs)

    return asyncio.run(send_request())


def test_health_endpoint():
    response = request("GET", "/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_endpoint_checks_database():
    response = request("GET", "/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_predict_endpoint_returns_transparent_baseline_mode():
    response = request(
        "POST",
        "/api/predict/",
        json={
            "night_purchase": True,
            "two_size_same_product": True,
            "customer_return_count": 3,
            "size_issue_score": 0.8,
            "unit_price": 900,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["risk_score"] == 1.0
    assert body["risk_level"] == "high"
    assert body["scoring_mode"] == "rules_baseline"
    assert len(body["top_factors"]) == 5


def test_missing_order_returns_not_found():
    response = request("GET", "/api/orders/99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}


def test_dashboard_summary_matches_scored_demo_batch():
    response = request("GET", "/api/dashboard/summary/")

    assert response.status_code == 200
    body = response.json()
    assert body["total_carts"] == 50
    assert body["high_risk"] == 13
    assert body["medium_risk"] == 18
    assert body["low_risk"] == 19
    assert body["high_risk_rate"] == 26.0


def test_dashboard_carts_are_sorted_and_limited():
    response = request("GET", "/api/dashboard/summary/carts?limit=3")

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 3
    assert body[0]["risk_score"] >= body[1]["risk_score"] >= body[2]["risk_score"]
    assert all(item["cart_id"].startswith("CART_") for item in body)


def test_read_only_agent_history_endpoints_return_lists():
    logs_response = request("GET", "/api/agent/logs")
    predictions_response = request("GET", "/api/agent/predictions?limit=3")

    assert logs_response.status_code == 200
    assert predictions_response.status_code == 200
    assert isinstance(logs_response.json(), list)
    assert isinstance(predictions_response.json(), list)


def test_analyze_cart_live_mode_uses_request_items(monkeypatch):
    class FakeOrchestrator:
        def __init__(self, db):
            self.db = db

        def analyze(self, cart_items, user_id, cart_id=None):
            assert cart_items[0]["product_id"] == "P1"
            assert user_id == 1
            assert cart_id == "LIVE_TEST"
            return {
                "risk_score": 0.7,
                "risk_level": "high",
                "scoring_mode": "rules_baseline",
                "agents_used": ["SignalAgent", "RiskAgent", "ActionAgent"],
                "reasons": ["two_size_same_product"],
                "customer_message": "Show size guidance.",
                "merchant_action": "show_size_guidance_before_checkout",
            }

    def override_db():
        yield object()

    monkeypatch.setattr(agent_routes, "get_cart_score", lambda cart_id: None)
    monkeypatch.setattr(agent_routes, "OrchestratorAgent", FakeOrchestrator)
    monkeypatch.setattr(agent_routes, "_persist_prediction", lambda db, result, cart_id: 101)
    monkeypatch.setattr(agent_routes, "add_log", lambda db, entry: None)
    app.dependency_overrides[get_db] = override_db

    try:
        response = request(
            "POST",
            "/api/agent/analyze-cart",
            json={
                "user_id": 1,
                "cart_id": "LIVE_TEST",
                "cart_items": [{"product_id": "P1", "size": "M", "price": 349, "hour": 23}],
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    body = response.json()
    assert body["analysis_mode"] == "live_rules"
    assert body["data_source"] == "database_and_request"
    assert body["input_items_used"] is True
    assert body["prediction_id"] == 101


def test_analyze_cart_demo_mode_uses_precomputed_score(monkeypatch):
    demo_result = {
        "cart_id": "CART_TEST",
        "analysis_mode": "demo_csv",
        "data_source": "agent_output_csv",
        "scoring_mode": "precomputed_agent_output",
        "score_type": "ranking_score_not_calibrated_probability",
        "risk_score": 0.87,
        "risk_level": "high",
        "agents_used": ["SignalAgent", "RiskAgent", "ActionAgent"],
        "reasons": ["high_transaction_model_rank"],
        "reason_details": [],
        "customer_message": "Show size and fit guidance.",
        "merchant_action": "show_size_guidance_before_checkout",
    }

    def override_db():
        yield object()

    monkeypatch.setattr(agent_routes, "get_cart_score", lambda cart_id: demo_result.copy())
    monkeypatch.setattr(agent_routes, "_persist_prediction", lambda db, result, cart_id: 102)
    monkeypatch.setattr(agent_routes, "add_log", lambda db, entry: None)
    app.dependency_overrides[get_db] = override_db

    try:
        response = request(
            "POST",
            "/api/agent/analyze-cart",
            json={"user_id": 1, "cart_id": "CART_TEST", "cart_items": []},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    body = response.json()
    assert body["analysis_mode"] == "demo_csv"
    assert body["scoring_mode"] == "precomputed_agent_output"
    assert body["input_items_used"] is False
    assert body["prediction_id"] == 102
