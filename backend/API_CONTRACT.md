# ReturnShield AI — API Contract

Base URL: http://localhost:8000

## Sprint 1 — Mevcut endpoint'ler

GET /api/orders
Response: [{id, product_name, product_size, unit_price, order_hour, is_returned, created_at}]

GET /api/orders/{id}
Response: tek sipariş objesi

GET /api/users
Response: [{id, name, email}]

## Sprint 2 — Eklenecek

POST /api/predict
Body: {order_id: int}
Response: {risk_score: float, risk_label: str, explanation: str}

POST /api/cart/analyze
Body: {user_id: int, items: [{product_name, size, hour}]}
Response: {risk_score: float, flags: [...], message: str}