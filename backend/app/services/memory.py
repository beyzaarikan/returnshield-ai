import json
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import AgentLog

def add_log(db: Session, entry: dict):
    record = AgentLog(
        cart_id=entry.get("cart_id"),
        user_id=entry.get("user_id"),
        risk_score=entry.get("risk_score"),
        risk_level=entry.get("risk_level"),
        analysis_mode=entry.get("analysis_mode"),
        data_source=entry.get("data_source"),
        agents_used=json.dumps(entry.get("agents_used", [])),
        reasons=json.dumps(entry.get("reasons", [])),
        customer_message=entry.get("customer_message"),
        merchant_action=entry.get("merchant_action"),
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return _serialize(record)

def get_logs(db: Session, limit: int = 50) -> List[dict]:
    rows = db.query(AgentLog).order_by(desc(AgentLog.created_at)).limit(limit).all()
    return [_serialize(row) for row in rows]

def _serialize(record: AgentLog) -> dict:
    return {
        "id": record.id,
        "cart_id": record.cart_id,
        "user_id": record.user_id,
        "risk_score": record.risk_score,
        "risk_level": record.risk_level,
        "analysis_mode": record.analysis_mode,
        "data_source": record.data_source,
        "agents_used": json.loads(record.agents_used or "[]"),
        "reasons": json.loads(record.reasons or "[]"),
        "customer_message": record.customer_message,
        "merchant_action": record.merchant_action,
        "timestamp": record.created_at.isoformat() if record.created_at else None,
    }
