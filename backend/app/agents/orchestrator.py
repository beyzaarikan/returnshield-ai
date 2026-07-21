from sqlalchemy.orm import Session
from app.agents.signal_agent import SignalAgent
from app.agents.risk_agent import RiskAgent
from app.agents.action_agent import ActionAgent

class OrchestratorAgent:
    """Runs Signal -> Risk -> Action in sequence and merges the results."""

    def __init__(self, db: Session, risk_model=None):
        self.signal_agent = SignalAgent(db)
        self.risk_agent = RiskAgent(model=risk_model)
        self.action_agent = ActionAgent()

    def analyze(self, cart_items: list, user_id: int, cart_id: str = None) -> dict:
        signals = self.signal_agent.extract(cart_items, user_id)
        risk_result = self.risk_agent.score(signals)
        action_result = self.action_agent.recommend(risk_result, cart_id=cart_id)

        return {
            "risk_score": risk_result["risk_score"],
            "risk_level": risk_result["risk_level"],
            "agents_used": ["SignalAgent", "RiskAgent", "ActionAgent"],
            "reasons": risk_result["top_factors"],
            "customer_message": action_result["customer_message"],
            "merchant_action": action_result["merchant_action"],
        }