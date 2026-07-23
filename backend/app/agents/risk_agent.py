class RiskAgent:
    """
    Calculates risk score from signals.
    Currently rule-based (baseline). Will switch to ML mode once model.pkl is ready.
    """

    def __init__(self, model=None):
        self.model = model  # TÜ2's pkl will be loaded here in Sprint 2

    def score(self, signals: dict) -> dict:
        if self.model:
            return self._score_with_model(signals)
        return self._score_with_rules(signals)

    def _score_with_rules(self, signals: dict) -> dict:
        score = 0.0
        reasons = []

        if signals.get("night_purchase"):
            score += 0.2
            reasons.append("Order was placed at night")

        if signals.get("two_size_same_product"):
            score += 0.3
            reasons.append("Same product added to cart in two different sizes")

        if signals.get("customer_return_count", 0) >= 3:
            score += 0.2
            reasons.append("Customer has 3+ past returns")

        if signals.get("size_issue_score", 0) > 0.5:
            score += 0.2
            reasons.append("High size mismatch signal in reviews")

        if signals.get("unit_price", 0) > 700:
            score += 0.1
            reasons.append("High-priced item increases expectation gap risk")

        score = min(score, 1.0)
        level = "high" if score >= 0.6 else "medium" if score >= 0.3 else "low"

        return {
            "risk_score": round(score, 2),
            "risk_level": level,
            "scoring_mode": "rules_baseline",
            "top_factors": reasons,
        }

    def _score_with_model(self, signals: dict) -> dict:
        # Fill this in once TÜ2's pkl is ready
        import pandas as pd
        features = pd.DataFrame([signals])
        proba = self.model.predict_proba(features)[0][1]
        level = "high" if proba >= 0.6 else "medium" if proba >= 0.3 else "low"
        return {
            "risk_score": round(float(proba), 2),
            "risk_level": level,
            "scoring_mode": "ml_model",
            "top_factors": [],
        }
