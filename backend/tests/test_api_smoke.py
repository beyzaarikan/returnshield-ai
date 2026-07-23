import asyncio

import httpx

from app.main import app


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
