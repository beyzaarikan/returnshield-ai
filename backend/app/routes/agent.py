from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.agents.orchestrator import OrchestratorAgent

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

@router.post("/analyze-cart")
def analyze_cart(payload: AnalyzeCartRequest, db: Session = Depends(get_db)):
    orchestrator = OrchestratorAgent(db)
    cart_items = [item.dict() for item in payload.cart_items]
    result = orchestrator.analyze(cart_items, payload.user_id)
    return result