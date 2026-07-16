class ActionAgent:
    """Generates a customer message and a merchant action based on the risk result."""

    CUSTOMER_TEMPLATES = {
        "high": "This item runs small for some customers. Would you like to check the size guide before purchasing?",
        "mid": "We recommend reviewing some customer feedback for this item.",
        "low": None,
    }

    MERCHANT_TEMPLATES = {
        "high": "Add fit information to the product description and highlight the size guide.",
        "mid": "Make the review summary more visible on the product page.",
        "low": "No action needed.",
    }

    def recommend(self, risk_result: dict) -> dict:
        level = risk_result["risk_level"]
        return {
            "customer_message": self.CUSTOMER_TEMPLATES.get(level),
            "merchant_action": self.MERCHANT_TEMPLATES.get(level),
        }