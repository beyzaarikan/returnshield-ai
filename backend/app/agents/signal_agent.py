from sqlalchemy.orm import Session
from app.models import Order

class SignalAgent:
    """Extracts a signal/feature dictionary from cart, customer history, and reviews."""

    def __init__(self, db: Session):
        self.db = db

    def extract(self, cart_items: list, user_id: int) -> dict:
        signals = {}

        # Cart behavior: same product, different size
        product_ids = [item["product_id"] for item in cart_items]
        signals["two_size_same_product"] = len(product_ids) != len(set(product_ids))

        # Night purchase
        hour = cart_items[0].get("hour", 12) if cart_items else 12
        signals["night_purchase"] = hour >= 22 or hour <= 2
        signals["order_hour"] = hour

        # Customer history
        past_returns = self.db.query(Order).filter(
            Order.user_id == user_id, Order.is_returned == True
        ).count()
        signals["customer_return_count"] = past_returns

        # Price
        signals["unit_price"] = max([item.get("price", 0) for item in cart_items], default=0)

        # Review signal (basic keyword check for now)
        signals["size_issue_score"] = self._check_size_complaints(cart_items)

        return signals

    def _check_size_complaints(self, cart_items: list) -> float:
        # This will later connect to TÜ2's fit_signals.csv lookup
        keywords = ["too small", "too tight", "runs small", "small fit"]
        for item in cart_items:
            desc = item.get("review_summary", "").lower()
            if any(k in desc for k in keywords):
                return 0.8
        return 0.1