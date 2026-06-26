from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import orders, users

app = FastAPI(title="ReturnShield AI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/")
def root():
    return {"status": "ok", "app": "ReturnShield AI"}