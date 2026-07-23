import os
from google import genai

class ActionAgent:
    """Generates a customer message and a merchant action based on the risk result."""

    CUSTOMER_TEMPLATES = {
        "high": "Fit-related signals are elevated for this item. We recommend checking the size guide and recent reviews before completing your purchase.",
        "medium": "Some customers have shared feedback about the fit of this item. Taking a moment to review the size guide may help you make the right choice.",
        "low": None,
    }

    CART_TEMPLATES = {
        "CART_0002": "This item has been added in two different sizes. Checking the size guide before purchasing may help you decide on the right fit.",
        "CART_0022": "Some customers noted length and color differences for this item compared to product photos. We recommend reviewing recent feedback before purchasing.",
        "CART_0007": "Your cart contains several items with length-related customer feedback. Reviewing each item's size guide may help avoid a return.",
        "CART_0036": "Based on fit signals and purchase patterns for these items, checking the size guide is recommended before completing your order.",
    }

    MERCHANT_TEMPLATES = {
        "high": "Add fit information to the product description and highlight the size guide.",
        "medium": "Make the review summary more visible on the product page.",
        "low": "No action needed.",
    }

    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY", "")
        self.use_llm = bool(api_key)
        if self.use_llm:
            self.client = genai.Client(api_key=api_key)

    def recommend(self, risk_result: dict, cart_id: str = None) -> dict:
        level = risk_result["risk_level"]
        reasons = risk_result.get("top_factors", [])

        if self.use_llm and level in ("high", "medium") and reasons:
            customer_message = self._generate_llm_message(level, reasons)
        elif cart_id and cart_id in self.CART_TEMPLATES:
            customer_message = self.CART_TEMPLATES[cart_id]
        else:
            customer_message = self.CUSTOMER_TEMPLATES.get(level)

        return {
            "customer_message": customer_message,
            "merchant_action": self.MERCHANT_TEMPLATES.get(level, "No action needed."),
        }

    def _generate_llm_message(self, level: str, reasons: list) -> str:
        try:
            reasons_text = ", ".join(
                r.replace("_", " ") if isinstance(r, str) else str(r)
                for r in reasons[:3]
            )
            prompt = (
                f"You are a helpful shopping assistant. "
                f"A customer is about to buy a fashion item. "
                f"Our system detected the following return risk signals: {reasons_text}. "
                f"Write a single short, friendly, non-accusatory message (1-2 sentences) "
                f"to gently inform the customer and suggest checking the size guide. "
                f"Do not mention 'risk', 'AI', or 'algorithm'. Keep it natural and helpful."
            )
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            print(f"Gemini error: {e}")
            return self.CUSTOMER_TEMPLATES.get(level)
