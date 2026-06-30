from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.risk_agent import RiskAgent

router = APIRouter()

class PredictRequest(BaseModel):
    night_purchase: bool = False
    two_size_same_product: bool = False
    customer_return_count: int = 0
    size_issue_score: float = 0.0
    unit_price: float = 0.0

@router.post("/")
def predict(payload: PredictRequest):
    agent = RiskAgent()
    return agent.score(payload.dict())