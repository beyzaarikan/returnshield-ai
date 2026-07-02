# ReturnShield Demo Cart Cases

This document lists selected cart examples for the ReturnShield MVP demo.

Main source file:

```text
outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
```

These cases are intended for the customer cart warning screen, merchant dashboard, and final presentation/video demo.

---

## 1. Selected demo cases

| Case | Cart ID | User | Risk score | Risk level | Suggested action | Demo use |
|---|---|---|---:|---|---|---|
| High-risk cart for the main customer warning demo | `CART_0022` | `MU_003` | 0.999 (100 / 100) | `high` | `show_size_guidance_before_checkout` | Main high-risk warning scenario |
| Medium-risk cart for comparison | `CART_0033` | `MU_019` | 0.851 (85 / 100) | `medium` | `show_size_guidance_before_checkout` | Show that not every cart is high risk |
| Low-risk cart for normal checkout comparison | `CART_0012` | `MU_028` | 0.638 (64 / 100) | `low` | `show_review_and_product_detail_summary` | Normal checkout / low-risk baseline |
| Review or product detail action case | `CART_0011` | `MU_028` | 0.747 (75 / 100) | `medium` | `show_review_and_product_detail_summary` | Review/product detail summary card |
| Color or product image action case | `CART_0028` | `MU_013` | 0.816 (82 / 100) | `medium` | `highlight_color_and_product_images` | Color/image detail warning card |

---

## 2. Detailed case notes

### Case 1: High-risk cart for the main customer warning demo

- **Cart ID:** `CART_0022`
- **Mock user ID:** `MU_003`
- **Risk score:** 0.999 (100 / 100)
- **Risk level:** `high`
- **Suggested action:** `show_size_guidance_before_checkout`
- **Dashboard/customer message:** Fit-related signals are elevated. Show size and fit guidance.
- **Top reasons:**
  - `high_transaction_model_rank`
  - `large_cart_size`
  - `length_issue_signal`
  - `rare_color_issue_review_flag`

**Recommended demo use:**
Use this as the main customer cart warning example. Show the risk badge, reasons, and suggested intervention.

### Case 2: Medium-risk cart for comparison

- **Cart ID:** `CART_0033`
- **Mock user ID:** `MU_019`
- **Risk score:** 0.851 (85 / 100)
- **Risk level:** `medium`
- **Suggested action:** `show_size_guidance_before_checkout`
- **Dashboard/customer message:** Multiple sizes of the same product are in the cart. Show size guidance before checkout.
- **Top reasons:**
  - `two_sizes_same_product`
  - `large_cart_size`
  - `fit_or_size_issue_signal`
  - `fit_layer_signal`

**Recommended demo use:**
Use this to show that the system can produce a moderate warning instead of classifying every cart as high risk.

### Case 3: Low-risk cart for normal checkout comparison

- **Cart ID:** `CART_0012`
- **Mock user ID:** `MU_028`
- **Risk score:** 0.638 (64 / 100)
- **Risk level:** `low`
- **Suggested action:** `show_review_and_product_detail_summary`
- **Dashboard/customer message:** Quality-related signals are elevated. Show product details and review summary.
- **Top reasons:**
  - `low_rating_signal_when_available`
  - `quality_issue_signal`

**Recommended demo use:**
Use this as the normal-checkout comparison case.

### Case 4: Review or product detail action case

- **Cart ID:** `CART_0011`
- **Mock user ID:** `MU_028`
- **Risk score:** 0.747 (75 / 100)
- **Risk level:** `medium`
- **Suggested action:** `show_review_and_product_detail_summary`
- **Dashboard/customer message:** Review signals are elevated. Show review summary before checkout.
- **Top reasons:**
  - `negative_review_language_signal`

**Recommended demo use:**
Use this to demonstrate review or product-detail explanation on the merchant/customer side.

### Case 5: Color or product image action case

- **Cart ID:** `CART_0028`
- **Mock user ID:** `MU_013`
- **Risk score:** 0.816 (82 / 100)
- **Risk level:** `medium`
- **Suggested action:** `highlight_color_and_product_images`
- **Dashboard/customer message:** Color issue appears in the review upper tail. Highlight product images and color details.
- **Top reasons:**
  - `duplicate_variant`
  - `high_transaction_model_rank`
  - `low_rating_signal_when_available`
  - `rare_color_issue_review_flag`

**Recommended demo use:**
Use this to demonstrate image/color detail highlighting.

---

## 3. Backend/frontend mapping

The backend can read the selected cart from `returnshield_agent_cart_scores.csv` and return it through an endpoint such as:

```text
GET /api/agent/analyze-cart/{cart_id}
```

Recommended response fields:

| API field | Source column |
|---|---|
| `cart_id` | `cart_id` |
| `mock_user_id` | `mock_user_id` |
| `risk_score` | `risk_score` |
| `risk_score_percent` | `risk_score * 100` |
| `risk_level` | `risk_level` |
| `reasons` | `top_reasons` |
| `suggested_action` | `suggested_action` |
| `customer_message` | `dashboard_message` |
| `merchant_action` | `suggested_action` |

---

## 4. Demo positioning

Use these cases to demonstrate the core ReturnShield idea:

```text
The system does not only predict a return risk score.
It explains why the cart may be risky and chooses a suitable intervention before checkout.
```

Recommended narrative:

1. Open a demo cart.
2. Show the risk score and risk level.
3. Show the main reasons.
4. Show the suggested action.
5. Show the customer-facing message or merchant dashboard action.

---

## 5. Limitations

- These cases are generated from the MVP demo pipeline.
- Mock carts are simulated and do not represent real production cart traffic.
- `risk_score` is a risk-ranking and decision-support score, not a calibrated return probability.
- The demo should not claim proven return reduction or production-level prediction accuracy.