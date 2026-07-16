from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import orders, users, agent, predict, summary

app = FastAPI(title="ReturnShield AI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(agent.router, prefix="/api/agent", tags=["agent"])
app.include_router(predict.router, prefix="/api/predict", tags=["predict"])
app.include_router(summary.router, prefix="/api/dashboard/summary", tags=["dashboard"])

@app.get("/")
def root():
    return {"status": "ok", "app": "ReturnShield AI"}