from types import SimpleNamespace

from app.agents.action_agent import ActionAgent
from app.config import settings


def high_risk_result():
    return {
        "risk_level": "high",
        "top_factors": ["two_size_same_product"],
    }


def test_action_agent_uses_template_without_gemini_key(monkeypatch):
    monkeypatch.setattr(settings, "GEMINI_API_KEY", "")

    result = ActionAgent().recommend(high_risk_result())

    assert result["message_source"] == "template"
    assert result["llm_used"] is False
    assert result["customer_message"]


def test_action_agent_uses_gemini_when_configured(monkeypatch):
    monkeypatch.setattr(settings, "GEMINI_API_KEY", "test-key")

    class FakeModels:
        def generate_content(self, **kwargs):
            assert kwargs["model"] == "gemini-2.0-flash"
            return SimpleNamespace(text="Please review the size guide before checkout.")

    class FakeClient:
        models = FakeModels()

    monkeypatch.setattr("app.agents.action_agent.genai.Client", lambda api_key: FakeClient())

    result = ActionAgent().recommend(high_risk_result())

    assert result["message_source"] == "gemini"
    assert result["llm_used"] is True
    assert result["customer_message"].startswith("Please review")


def test_action_agent_falls_back_when_gemini_fails(monkeypatch):
    monkeypatch.setattr(settings, "GEMINI_API_KEY", "test-key")

    class FailingModels:
        def generate_content(self, **kwargs):
            raise RuntimeError("simulated Gemini failure")

    class FakeClient:
        models = FailingModels()

    monkeypatch.setattr("app.agents.action_agent.genai.Client", lambda api_key: FakeClient())

    result = ActionAgent().recommend(high_risk_result())

    assert result["message_source"] == "template"
    assert result["llm_used"] is False
    assert result["customer_message"]
