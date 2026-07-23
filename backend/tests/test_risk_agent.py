from app.agents.risk_agent import RiskAgent


def test_empty_signals_are_low_risk():
    result = RiskAgent().score({})

    assert result["risk_score"] == 0.0
    assert result["risk_level"] == "low"


def test_medium_signals_use_standard_label():
    result = RiskAgent().score({
        "two_size_same_product": True,
    })

    assert result["risk_score"] == 0.3
    assert result["risk_level"] == "medium"
    assert result["top_factors"]


def test_combined_signals_reach_high_risk():
    result = RiskAgent().score({
        "night_purchase": True,
        "two_size_same_product": True,
        "customer_return_count": 3,
        "size_issue_score": 0.8,
        "unit_price": 900,
    })

    assert result["risk_score"] == 1.0
    assert result["risk_level"] == "high"
