# ReturnShield Agent Output Schema

This document explains how the backend and frontend should use the final Risk Agent demo output.

Main file:

```text
outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
```

This file is produced by:

```text
notebooks/06_returnshield_agent_demo.ipynb
```

It contains one row per demo cart. Each row already includes the final risk score, risk level, risk reasons, suggested action, and dashboard/customer-facing message.

---

## 1. Purpose

The purpose of this output is to connect the Data/ML pipeline to the web application.

The Data/ML side provides:

```text
cart-level risk analysis
+ explanation reasons
+ suggested intervention
+ dashboard/customer message
```

The backend/frontend side should use this file to display:

- risk badge,
- risk score,
- reason list,
- suggested action,
- customer-facing warning card,
- merchant/dashboard action.

This output supports the project flow:

```text
cart analysis -> risk score -> reason explanation -> suggested intervention
```

---

## 2. Main output file

| Field | Value |
|---|---|
| File path | `outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv` |
| Producer | `06_returnshield_agent_demo.ipynb` |
| Granularity | One row per cart |
| Main key | `cart_id` |
| Main consumer | Backend API / frontend dashboard |
| Data type | CSV |
| Intended use | Demo/API response source |

---

## 3. Minimum columns for backend/frontend

These are the most important fields for the web application.

| Column | Type | Description | Frontend/backend use |
|---|---|---|---|
| `cart_id` | string | Demo cart identifier | Used to select or query a cart |
| `mock_user_id` | string | Simulated user identifier | Optional display/filter field |
| `risk_score` | float | Final Risk Agent score between 0 and 1 | Risk score badge/card |
| `risk_percentile_rank` | float | Percentile rank within the demo cart batch | Optional ranking explanation |
| `risk_level` | string | Risk level: `low`, `medium`, or `high` | Risk badge |
| `top_reasons` | JSON string/list | Main reason codes for the risk result | Reason list |
| `reason_details` | JSON string/list | Reason code, severity, and explanation details | Detailed explanation panel |
| `suggested_action` | string | Action code selected by the agent | Action card / UI behavior |
| `dashboard_message` | string | Human-readable explanation/action message | Customer warning card or merchant panel |

---

## 4. Recommended API response

The backend can expose the CSV row through an endpoint such as:

```text
GET /api/agent/analyze-cart/{cart_id}
```

or:

```text
POST /api/agent/analyze-cart
```

Recommended response shape:

```json
{
  "cart_id": "CART_0001",
  "mock_user_id": "USER_001",
  "risk_score": 0.82,
  "risk_score_percent": 82,
  "risk_level": "high",
  "reasons": [
    "high_transaction_model_rank",
    "fit_or_size_issue_signal",
    "large_cart_size"
  ],
  "reason_details": [
    {
      "code": "high_transaction_model_rank",
      "severity": 0.91,
      "message": "Transaction model rank is high."
    },
    {
      "code": "fit_or_size_issue_signal",
      "severity": 0.76,
      "message": "Fit or size mismatch signal is elevated."
    }
  ],
  "suggested_action": "show_size_guidance_before_checkout",
  "customer_message": "Fit-related signals are elevated. Show size and fit guidance.",
  "merchant_action": "show_size_guidance_before_checkout"
}
```

Mapping from CSV to API response:

| CSV column | API field | Note |
|---|---|---|
| `cart_id` | `cart_id` | Same value |
| `mock_user_id` | `mock_user_id` | Same value |
| `risk_score` | `risk_score` | Keep 0-1 value |
| `risk_score` | `risk_score_percent` | Optional: multiply by 100 and round |
| `risk_level` | `risk_level` | Same value |
| `top_reasons` | `reasons` | Parse JSON string if needed |
| `reason_details` | `reason_details` | Parse JSON string if needed |
| `suggested_action` | `suggested_action` | Same value |
| `dashboard_message` | `customer_message` | Can be shown on customer cart screen |
| `suggested_action` | `merchant_action` | Can be used as merchant-side action code |

---

## 5. Risk score interpretation

| Field | Meaning |
|---|---|
| `risk_score` | Final Risk Agent score in the 0-1 range |
| `risk_level` | Relative demo risk level: `low`, `medium`, `high` |
| `label_backed_risk_score` | Transaction-model anchor component |
| `contextual_evidence_score` | Fit/review/cart contextual evidence component |

Important interpretation:

```text
risk_score is not a calibrated probability of return.
It is an MVP risk-ranking and decision-support score.
```

Recommended UI display:

| Risk level | UI label | Suggested badge |
|---|---|---|
| `low` | Low return risk | Green/neutral badge |
| `medium` | Medium return risk | Yellow/orange badge |
| `high` | High return risk | Red/highlighted badge |

Example frontend display:

```text
Return risk: High
Risk score: 82 / 100
Main reasons:
- Fit or size mismatch signal is elevated.
- Cart size is high for this demo batch.
Suggested action:
Show size guidance before checkout.
```

---

## 6. Suggested action values

| Value | Meaning | Suggested frontend behavior |
|---|---|---|
| `show_size_guidance_before_checkout` | Size/fit risk is detected | Show size guide, fit note, or size recommendation card |
| `highlight_color_and_product_images` | Color/visual mismatch signal is detected | Show product images, color note, or visual detail card |
| `show_review_and_product_detail_summary` | Review/quality/rating signal is detected | Show review summary and product detail note |
| `confirm_duplicate_variant` | Same variant appears more than once | Ask user to confirm repeated item |
| `show_return_policy_and_checkout_confirmation` | Transaction risk is high but no specific fit/review action dominates | Show return policy or checkout confirmation |
| `standard_checkout` | No strong risk action detected | Continue normal checkout |

---

## 7. Reason codes

| Reason code | Meaning | Suggested UI text |
|---|---|---|
| `high_transaction_model_rank` | Transaction model rank is high | This cart has a high transaction-level return/cancel risk signal. |
| `fit_layer_signal` | Fit layer signal is elevated | Fit-related product signals are elevated. |
| `fit_or_size_issue_signal` | Fit or size mismatch signal is elevated | Some signals suggest possible size or fit mismatch. |
| `length_issue_signal` | Length issue signal is elevated | Some users reported length-related issues. |
| `quality_issue_signal` | Quality/material issue signal is elevated | Review or fit signals suggest possible quality concerns. |
| `negative_review_language_signal` | Negative review language signal is elevated | Reviews contain relatively stronger negative wording. |
| `rare_color_issue_review_flag` | Color issue appears in the upper tail | Some reviews suggest color or visual mismatch. |
| `low_rating_signal_when_available` | Rating issue is elevated when rating exists | Rating-based dissatisfaction signal is elevated. |
| `two_sizes_same_product` | Same product appears in two sizes | The cart contains multiple sizes of the same product. |
| `duplicate_variant` | Same variant appears more than once | The cart contains a repeated variant. |
| `large_cart_size` | Cart size is high | The cart is large relative to the demo batch. |
| `dominant_transaction_model_signal` | Transaction model is the strongest available layer | The transaction model is the dominant available signal. |
| `dominant_fit_signal` | Fit is the strongest available layer | Fit-related evidence is the dominant available signal. |
| `dominant_review_text_signal` | Review text is the strongest available layer | Review text evidence is the dominant available signal. |
| `dominant_cart_behavior_signal` | Cart behavior is the strongest available layer | Cart behavior is the dominant available signal. |

---

## 8. Customer-facing message guidance

The frontend can directly display `dashboard_message`, but the final wording should follow these rules:

- Do not blame the user.
- Do not block the purchase.
- Do not use pressure or fear language.
- Do not claim that a return will definitely happen.
- Present the message as a helpful checkout decision support.

Recommended examples:

| Situation | Customer-facing message |
|---|---|
| Size/fit signal | `Some size or fit signals are elevated for this cart. You may want to check the size guide before checkout.` |
| Review/quality signal | `Some review signals suggest quality or product-detail concerns. You may want to review the product details before checkout.` |
| Color signal | `Some reviews mention color or visual differences. You may want to check product images before checkout.` |
| Transaction-only risk | `This cart has a higher return-risk signal. You may want to review the item details before completing checkout.` |
| Low risk | `No strong return-risk reason was detected for this cart.` |

---

## 9. Merchant/dashboard use

For the merchant dashboard, show:

- high-risk carts,
- top risk reasons,
- suggested actions,
- model/context breakdown,
- action distribution.

Recommended dashboard columns:

| UI column | Source column |
|---|---|
| Cart ID | `cart_id` |
| User | `mock_user_id` |
| Risk score | `risk_score` |
| Risk level | `risk_level` |
| Reasons | `top_reasons` or `reason_details` |
| Suggested action | `suggested_action` |
| Message | `dashboard_message` |
| Transaction component | `label_backed_risk_score` |
| Context component | `contextual_evidence_score` |

---

## 10. Optional technical fields

These fields are useful for explainability/debugging but are not mandatory in the first frontend version.

| Column | Meaning |
|---|---|
| `label_backed_risk_score` | Transaction model anchor component |
| `contextual_evidence_score` | Fit/review/cart contextual evidence score |
| `context_signal_count` | Number of contextual evidence flags |
| `risk_input_coverage_weight` | Available input weight used during scoring |
| `transaction_layer_score` | Transaction layer score |
| `fit_layer_agent_score` | Fit layer score used by the agent |
| `review_layer_agent_score` | Review layer score used by the agent |
| `cart_behavior_agent_score` | Cart behavior score used by the agent |
| `fit_context_evidence_score` | Fit context evidence |
| `review_context_evidence_score` | Review context evidence |
| `cart_context_evidence_score` | Cart context evidence |

---

## 11. Minimal frontend requirements

A minimum useful demo screen should show:

1. Cart ID
2. Risk score as percentage
3. Risk level badge
4. Main reasons
5. Suggested action
6. Customer-facing message

Minimum UI example:

```text
Cart: CART_0001
Risk: High — 82/100

Why this cart is risky:
- Fit or size mismatch signal is elevated.
- Cart size is high for this demo batch.

Suggested action:
Show size guidance before checkout.

Message:
Fit-related signals are elevated. Show size and fit guidance.
```

---

## 12. Limitations

- The output is based on an MVP data/ML prototype.
- `risk_score` is not a calibrated return probability.
- Mock carts are simulated for demo purposes.
- UCI Online Retail and fashion review items are not true row-level product matches.
- The output should be used as decision support, not as an automatic purchase-blocking decision.
- If an LLM is added later, it should only rewrite or personalize approved messages. It should not independently decide the risk level or action.

---

## 13. Backend implementation note

For the MVP, the backend does not need to retrain the model.

Recommended simple flow:

```text
load returnshield_agent_cart_scores.csv
filter by cart_id
parse top_reasons and reason_details
return API response
```

Pseudo-code:

```python
import json
import pandas as pd

df = pd.read_csv("outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv")

def analyze_cart(cart_id: str) -> dict:
    row = df.loc[df["cart_id"] == cart_id].iloc[0]

    return {
        "cart_id": row["cart_id"],
        "mock_user_id": row["mock_user_id"],
        "risk_score": float(row["risk_score"]),
        "risk_score_percent": round(float(row["risk_score"]) * 100),
        "risk_level": row["risk_level"],
        "reasons": json.loads(row["top_reasons"]),
        "reason_details": json.loads(row["reason_details"]),
        "suggested_action": row["suggested_action"],
        "customer_message": row["dashboard_message"],
        "merchant_action": row["suggested_action"],
    }
```

This is enough for the frontend to build the customer cart warning and merchant dashboard panels.
