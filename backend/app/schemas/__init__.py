from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_name: str
    product_size: Optional[str]
    quantity: int
    unit_price: float
    order_hour: int
    is_returned: bool
    created_at: datetime
    customer_name: str | None = None

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
