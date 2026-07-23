from fastapi import APIRouter
from pydantic import BaseModel
from app.services.cart_scores import load_cart_scores
import pandas as pd

router = APIRouter()

class CartDashboardOut(BaseModel):
    cart_id: str
    customer_name: str
    product_name: str
    order_hour: str
    risk_score: float
    risk_level: str
    is_returned: bool = False

@router.get("/carts", response_model=list[CartDashboardOut])
def dashboard_carts(limit: int = 10):
    df = load_cart_scores()
    if df is None:
        return []

    limit = max(1, min(limit, 50))
    rows = df.nlargest(limit, "risk_score")
    return [
        {
            "cart_id": str(row["cart_id"]),
            "customer_name": f"Demo customer {row['mock_user_id']}",
            "product_name": str(row["primary_mock_product_id"]),
            "order_hour": "Night" if float(row["night_purchase"]) else "Day",
            "risk_score": round(float(row["risk_score"]), 2),
            "risk_level": str(row["risk_level"]),
        }
        for _, row in rows.iterrows()
    ]

@router.get("/")
def dashboard_summary():
    df = load_cart_scores()
    if df is None:
        return {"total_carts": 0, "high_risk": 0, "medium_risk": 0, "low_risk": 0, "high_risk_rate": 0, "returns_prevented_est": 0, "co2_saved_kg": 0}

    total = len(df)
    high = int((df["risk_level"] == "high").sum())
    medium = int((df["risk_level"] == "medium").sum())
    low = int((df["risk_level"] == "low").sum())
    prevented = round(high * 0.7)
    co2 = round(prevented * 2.3, 1)

    return {
        "total_carts": total,
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low,
        "high_risk_rate": round(high / total * 100, 1) if total else 0,
        "returns_prevented_est": prevented,
        "co2_saved_kg": co2
    }
