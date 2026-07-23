# backend/app/services/cart_scores.py
import pandas as pd
import json
import os

_df = None

def load_cart_scores():
    global _df
    if _df is None:
        path = "/outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv"
        if not os.path.exists(path):
            return None
        _df = pd.read_csv(path)
    return _df

def get_cart_score(cart_id: str):
    df = load_cart_scores()
    if df is None:
        return None
    row = df[df["cart_id"] == cart_id]
    if row.empty:
        return None
    r = row.iloc[0]

    try:
        reasons = json.loads(r["top_reasons"]) if pd.notna(r["top_reasons"]) else []
    except Exception:
        reasons = []

    try:
        reason_details = json.loads(r["reason_details"]) if pd.notna(r["reason_details"]) else []
    except Exception:
        reason_details = []

    return {
        "cart_id": cart_id,
        "analysis_mode": "demo_csv",
        "data_source": "agent_output_csv",
        "scoring_mode": "precomputed_agent_output",
        "score_type": "ranking_score_not_calibrated_probability",
        "risk_score": round(float(r["risk_score"]), 2),
        "risk_level": str(r["risk_level"]),
        "agents_used": ["SignalAgent", "RiskAgent", "ActionAgent"],
        "reasons": reasons,
        "reason_details": reason_details,
        "customer_message": str(r["dashboard_message"]) if pd.notna(r["dashboard_message"]) else None,
        "merchant_action": str(r["suggested_action"]) if pd.notna(r["suggested_action"]) else None,
        "message_source": "precomputed_agent_output",
        "llm_used": False,
    }
