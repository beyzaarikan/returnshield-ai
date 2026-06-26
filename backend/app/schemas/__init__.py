from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderOut(BaseModel):
    id: int
    product_name: str
    product_size: Optional[str]
    unit_price: float
    order_hour: int
    is_returned: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True