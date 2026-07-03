from fastapi import APIRouter
from app.services.cart_scores import load_cart_scores
import pandas as pd

router = APIRouter()

@router.get("/")
def dashboard_summary():
    df = load_cart_scores()
    if df is None:
        return {"total_carts": 0, "high_risk": 0, "medium_risk": 0, "low_risk": 0, "returns_prevented_est": 0, "co2_saved_kg": 0}

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
        "returns_prevented_est": prevented,
        "co2_saved_kg": co2
    }