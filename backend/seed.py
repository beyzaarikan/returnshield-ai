from app.database import SessionLocal
from app.models import User, Order

def seed():
    db = SessionLocal()

    users = [
        User(name="Alice Johnson", email="alice@demo.com"),
        User(name="Michael Smith", email="michael@demo.com"),
        User(name="Sarah Wilson", email="sarah@demo.com"),
    ]
    db.add_all(users)
    db.commit()
    for u in users:
        db.refresh(u)

    orders = [
        Order(user_id=users[0].id, product_name="Oversized Sweatshirt",
              product_size="M", quantity=1, unit_price=349.0,
              order_hour=23, is_returned=True),
        Order(user_id=users[0].id, product_name="Oversized Sweatshirt",
              product_size="L", quantity=1, unit_price=349.0,
              order_hour=23, is_returned=False),
        Order(user_id=users[1].id, product_name="Slim Fit Trousers",
              product_size="32", quantity=1, unit_price=499.0,
              order_hour=14, is_returned=False),
        Order(user_id=users[2].id, product_name="Dress",
              product_size="S", quantity=1, unit_price=799.0,
              order_hour=1, is_returned=True),
        Order(user_id=users[2].id, product_name="Dress",
              product_size="M", quantity=1, unit_price=799.0,
              order_hour=1, is_returned=False),
    ]
    db.add_all(orders)
    db.commit()
    print("Seed completed.")
    db.close()

if __name__ == "__main__":
    seed()