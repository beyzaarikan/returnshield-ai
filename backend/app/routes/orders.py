from fastapi import APIRouter, Depends, HTTPException
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
            "quantity": o.quantity,
            "unit_price": o.unit_price,
            "order_hour": o.order_hour,
            "is_returned": o.is_returned,
            "created_at": o.created_at,
            "customer_name": user.name if user else "Unknown"
        }
        result.append(o_dict)
    return result

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)) -> OrderOut:
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    user = db.query(User).filter(User.id == order.user_id).first()
    return {
        "id": order.id,
        "product_name": order.product_name,
        "product_size": order.product_size,
        "quantity": order.quantity,
        "unit_price": order.unit_price,
        "order_hour": order.order_hour,
        "is_returned": order.is_returned,
        "created_at": order.created_at,
        "customer_name": user.name if user else "Unknown",
    }
