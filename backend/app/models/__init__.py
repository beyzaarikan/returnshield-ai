from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String)
    product_size = Column(String, nullable=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    order_hour = Column(Integer)
    is_returned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="orders")

class ReturnPrediction(Base):
    __tablename__ = "return_predictions"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    cart_id = Column(String, nullable=True, index=True)
    risk_score = Column(Float)
    risk_label = Column(String)
    explanation = Column(String, nullable=True)
    analysis_mode = Column(String, nullable=True)
    score_type = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class AgentLog(Base):
    __tablename__ = "agent_logs"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(String, nullable=True, index=True)
    user_id = Column(Integer, nullable=True)
    risk_score = Column(Float, nullable=True)
    risk_level = Column(String, nullable=True)
    analysis_mode = Column(String, nullable=True)
    data_source = Column(String, nullable=True)
    agents_used = Column(Text, nullable=True)
    reasons = Column(Text, nullable=True)
    customer_message = Column(Text, nullable=True)
    merchant_action = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
