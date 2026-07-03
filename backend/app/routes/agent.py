from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.agents.orchestrator import OrchestratorAgent
from app.services.cart_scores import get_cart_score

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
            return result

    # CSV'de yoksa kural tabanlı devam et
    orchestrator = OrchestratorAgent(db)
    cart_items = [item.dict() for item in payload.cart_items]
    return orchestrator.analyze(cart_items, payload.user_id)

@router.get("/top-alerts")
def top_alerts():
    from app.services.cart_scores import load_cart_scores
    import json
    df = load_cart_scores()
    if df is None:
        return []

    top = df.nlargest(4, "risk_score")
    result = []
    for _, row in top.iterrows():
        level = str(row["risk_level"])
        level_display = "high" if level == "high" else "mid"
        try:
            reasons = json.loads(row["top_reasons"])
            first_reason = reasons[0].replace("_", " ").title() if reasons else "Risk detected"
        except:
            first_reason = "Risk detected"

        result.append({
            "level": level_display,
            "name": f"{row['cart_id']} — {first_reason}",
            "desc": str(row["dashboard_message"]) if str(row["dashboard_message"]) != "nan" else "High return risk detected."
        })
    return result