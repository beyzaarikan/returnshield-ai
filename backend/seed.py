from app.database import SessionLocal
from app.models import User, Order

def seed():
    db = SessionLocal()
    try:
        user_data = [
            ("Alice Johnson", "alice@demo.com"),
            ("Michael Smith", "michael@demo.com"),
            ("Sarah Wilson", "sarah@demo.com"),
        ]
        users = {}
        for name, email in user_data:
            user = db.query(User).filter(User.email == email).first()
            if user is None:
                user = User(name=name, email=email)
                db.add(user)
                db.flush()
            users[email] = user

        order_data = [
            ("alice@demo.com", "Oversized Sweatshirt", "M", 1, 349.0, 23, True),
            ("alice@demo.com", "Oversized Sweatshirt", "L", 1, 349.0, 23, False),
            ("michael@demo.com", "Slim Fit Trousers", "32", 1, 499.0, 14, False),
            ("sarah@demo.com", "Dress", "S", 1, 799.0, 1, True),
            ("sarah@demo.com", "Dress", "M", 1, 799.0, 1, False),
        ]
        for email, product, size, quantity, price, hour, returned in order_data:
            exists = db.query(Order).filter(
                Order.user_id == users[email].id,
                Order.product_name == product,
                Order.product_size == size,
                Order.order_hour == hour,
            ).first()
            if exists is None:
                db.add(Order(
                    user_id=users[email].id,
                    product_name=product,
                    product_size=size,
                    quantity=quantity,
                    unit_price=price,
                    order_hour=hour,
                    is_returned=returned,
                ))

        db.commit()
        print("Seed completed without duplicate records.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed()
