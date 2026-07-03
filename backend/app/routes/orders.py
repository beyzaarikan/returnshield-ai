from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, User
from app.schemas import OrderOut
from typing import List

router = APIRouter()

@router.get("/", response_model=List[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    result = []
    for o in orders:
        user = db.query(User).filter(User.id == o.user_id).first()
        o_dict = {
            "id": o.id,
            "product_name": o.product_name,
            "product_size": o.product_size,
            "unit_price": o.unit_price,
            "order_hour": o.order_hour,
            "is_returned": o.is_returned,
            "created_at": o.created_at,
            "customer_name": user.name if user else "Unknown"
        }
        result.append(o_dict)
    return result

@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.id == order_id).first()