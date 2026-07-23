from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.agents.orchestrator import OrchestratorAgent
from app.services.cart_scores import get_cart_score
from app.services.memory import add_log, get_logs

router = APIRouter()

class CartItem(BaseModel):
    product_id: str
    size: str | None = None
    price: float = 0
    hour: int = 12
    review_summary: str = ""

class AnalyzeCartRequest(BaseModel):
    user_id: int
    cart_items: list[CartItem]
    cart_id: str | None = None  # demo cart_id varsa CSV'den okur


@router.post("/analyze-cart")
def analyze_cart(payload: AnalyzeCartRequest, db: Session = Depends(get_db)):
    # Önce CSV'den bak
    if payload.cart_id:
        result = get_cart_score(payload.cart_id)
        if result:
            result["input_items_used"] = False
            add_log({
                "cart_id": payload.cart_id,
                "user_id": payload.user_id,
                "risk_score": result["risk_score"],
                "risk_level": result["risk_level"],
                "agents_used": result["agents_used"],
                "reasons": result["reasons"],
                "customer_message": result["customer_message"],
            })
            return result

    # CSV'de yoksa kural tabanlı devam et
    orchestrator = OrchestratorAgent(db)
    cart_items = [item.dict() for item in payload.cart_items]
    result = orchestrator.analyze(cart_items, payload.user_id, cart_id=payload.cart_id)
    result.update({
        "analysis_mode": "live_rules",
        "data_source": "database_and_request",
        "score_type": "rule_score_not_calibrated_probability",
        "input_items_used": True,
    })
    add_log({
        "cart_id": payload.cart_id or "live",
        "user_id": payload.user_id,
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "agents_used": result["agents_used"],
        "reasons": result["reasons"],
        "customer_message": result["customer_message"],
    })
    return result

@router.get("/logs")
def get_agent_logs():
    return get_logs()

@router.get("/top-alerts")
def top_alerts():
    from app.services.cart_scores import load_cart_scores
    import json
    df = load_cart_scores()
    if df is None:
        return []

    REASON_LABELS = {
        "high_transaction_model_rank": "High return risk history",
        "two_sizes_same_product": "Two sizes of same product",
        "large_cart_size": "Large cart — uncertainty signal",
        "length_issue_signal": "Length issue in reviews",
        "quality_issue_signal": "Quality complaints in reviews",
        "fit_or_size_issue_signal": "Fit/size issue detected",
        "rare_color_issue_review_flag": "Color mismatch in reviews",
        "duplicate_variant": "Duplicate product variant",
        "fit_layer_signal": "Fit signal elevated",
        "low_rating_signal_when_available": "Low rating signal",
        "high_return_history": "High return history",
        "review_text_size_issue": "Size issue in reviews",
        "review_text_quality_issue": "Quality issue in reviews",
        "review_text_color_issue": "Color issue in reviews",
    }

    top = df.nlargest(4, "risk_score")
    result = []
    for _, row in top.iterrows():
        level = str(row["risk_level"])
        level_display = level if level in {"high", "medium", "low"} else "medium"

        try:
            reasons = json.loads(row["top_reasons"])
            first_reason = REASON_LABELS.get(reasons[0], reasons[0].replace("_", " ").title()) if reasons else "Risk detected"
        except:
            first_reason = "Risk detected"

        customer_id = str(row["mock_user_id"])
        name = f"Customer {customer_id} — {first_reason}"

        desc = str(row["dashboard_message"]) if str(row["dashboard_message"]) != "nan" else "High return risk detected."

        result.append({
            "level": level_display,
            "name": name,
            "desc": desc
        })
    return result
