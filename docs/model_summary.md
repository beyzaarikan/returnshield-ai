# ReturnShield Model Summary

This document summarizes the data/ML and Risk Agent results of the ReturnShield MVP.

ReturnShield is not positioned as a production-grade return prediction system. The current model layer is used as an MVP risk-ranking component that supports an agentic decision flow:

```text
cart analysis -> risk score -> reason explanation -> suggested intervention
```

---

## 1. Goal

The goal of the data/ML pipeline is to identify return-risk signals before checkout and convert them into an explainable agent output.

The pipeline produces:

- transaction-based return/cancel risk ranking,
- fit, length, quality, review, rating, and cart behavior signals,
- cart-level demo features,
- Risk Agent outputs: `risk_score`, `risk_level`, `top_reasons`, `suggested_action`, and `dashboard_message`.

The system is designed as a decision-support layer, not as an automatic purchase blocker.

---

## 2. Data sources

| Source | Role in the project | Status |
|---|---|---|
| UCI Online Retail | Transaction layer, return/cancel proxy label, baseline risk model | Open/raw data |
| ModCloth Clothing Fit | Fit, length, quality, rating, and review signals | Open/raw data |
| RentTheRunway Clothing Fit | Fit, length, quality, rating, and review signals | Open/raw data |
| Mock cart generation | Cart-level MVP demo input | Simulated |

Important note:

UCI Online Retail and the fashion review datasets are not treated as true row-level product matches. The project uses a controlled mock mapping only for demo purposes.

---

## 3. Notebook pipeline

| Notebook | Purpose | Main output |
|---|---|---|
| `01_online_retail_data_preparation.ipynb` | Cleans Online Retail data and creates the return/cancel proxy label | `online_retail_model_base.csv` |
| `02_online_retail_baseline_modeling.ipynb` | Trains and evaluates baseline transaction risk models | model metrics, top-k lift, `online_retail_test_scores.csv` |
| `03_fit_signal_poc.ipynb` | Builds item-level fit, length, and quality signals | `fit_signals.csv` |
| `04_review_signal_poc.ipynb` | Builds review-text, rating, color, quality, and negative-language signals | `review_signals.csv`, `review_signal_handoff.csv` |
| `05_mock_cart_features.ipynb` | Combines transaction, fit, review, and cart signals into cart-level demo features | `mock_cart_features.csv` |
| `06_returnshield_agent_demo.ipynb` | Produces Risk Agent score, risk level, reasons, actions, and dashboard messages | `returnshield_agent_cart_scores.csv` |

---

## 4. Label definition

The transaction model uses a derived return/cancel proxy label.

| Field | Meaning |
|---|---|
| `is_return` | Derived return/cancel proxy label from the Online Retail transaction data |

This is not a real production return label from an e-commerce company's internal system. It is a proxy label derived from open transaction data. Therefore, the model should be interpreted as a risk-ranking baseline rather than a calibrated return-probability model.

---

## 5. Modeling approach

The baseline modeling step compares transaction-level models and selects the best-performing risk-ranking layer for the MVP.

Selected model:

```text
rf_history_smoothed
```

The selected transaction model is used downstream through:

```text
selected_model_score -> model_risk_rank_score -> transaction_layer_score
```

The final Risk Agent score is transaction-anchored and context-aware:

```text
risk_score = label-backed transaction anchor + contextual evidence
```

Contextual evidence comes from fit, review, and cart behavior signals.

---

## 6. Main model metrics

The return/cancel label is highly imbalanced, so accuracy is not the main evaluation metric. PR-AUC, ROC-AUC, precision-at-top-k, and lift are more relevant for this MVP.

| Metric | Value | Interpretation |
|---|---:|---|
| Test PR-AUC | 0.049 | Better than the low positive-class base rate; useful for ranking but not a production classifier. |
| Test ROC-AUC | 0.753 | The model separates higher-risk and lower-risk transactions reasonably well. |
| Test base rate | 0.0125 | The positive class is rare, so the task is highly imbalanced. |
| Top 1% precision | 0.1068 | The highest-risk 1% contains returns/cancellations at a much higher rate than the base rate. |
| Top 1% lift | 8.56x | The top 1% risk group is about 8.56 times richer in positive cases than the average test population. |
| Top 5% lift | 5.33x | The top 5% risk group remains meaningfully enriched. |
| Top 10% lift | 3.94x | The model still provides useful ranking power in the top 10%. |

Summary:

The model is not used to claim exact return probability. Its value is that it ranks high-risk transactions better than random selection in a highly imbalanced problem.

---

## 7. Why accuracy is not emphasized

The return/cancel proxy label has a very low positive rate. In this setting, a model can achieve high accuracy by predicting almost everything as non-return.

For this reason, ReturnShield focuses on:

- PR-AUC,
- ROC-AUC,
- top-k precision,
- lift over base rate,
- explanation quality,
- actionability of the output.

This is aligned with the product goal: finding high-risk carts early enough to support a better checkout decision.

---

## 8. Fit and review signal results

The fit and review notebooks build additional product-context signals.

| Signal group | Example fields | Role |
|---|---|---|
| Fit signal | `item_fit_issue_score`, `item_length_issue_score` | Explains size and fit-related risk |
| Quality signal | `item_quality_issue_score`, `review_text_quality_issue_score` | Explains material/product satisfaction risk |
| Review text signal | `review_text_size_issue_score`, `review_text_negative_language_score` | Extracts risk reasons from user reviews |
| Rating signal | `rating_issue_score` | Adds rating-based dissatisfaction evidence when available |
| Color signal | `review_text_color_issue_score_upper_tail_flag` | Used mainly as an explanation/flag, not as a dominant continuous score |

Important note:

Missing fit, review, or rating evidence is not treated as low risk. Availability fields such as `fit_signal_available`, `review_signal_available`, and `rating_signal_available` are used to avoid misleading interpretation.

---

## 9. Mock cart feature layer

Notebook 05 creates a controlled demo cart layer.

Main output:

```text
data/processed/mock_cart_features.csv
```

| Field | Meaning |
|---|---|
| `cart_id` | Demo cart identifier |
| `mock_user_id` | Simulated user identifier |
| `model_risk_rank_score` | Transaction model risk rank used by the Risk Agent |
| `fit_layer_summary_score` | Cart-level fit signal summary |
| `review_text_summary_score` | Cart-level review signal summary |
| `two_size_same_product` | Whether the same product appears with two different sizes |
| `duplicate_variant` | Whether the same variant appears more than once |
| `cart_uncertainty_signal_count` | Count of cart uncertainty signals |
| `cart_size_pressure` | Cart-size based contextual signal |

Important note:

The mock cart layer is used to demonstrate agent behavior. It is not a real production cart dataset.

---

## 10. Risk Agent output

Notebook 06 produces the final demo output:

```text
outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
```

| Field | Meaning |
|---|---|
| `risk_score` | Final Risk Agent score between 0 and 1 |
| `risk_level` | `low`, `medium`, or `high` |
| `label_backed_risk_score` | Transaction-model anchor component |
| `contextual_evidence_score` | Fit/review/cart contextual evidence component |
| `top_reasons` | Main reason codes behind the risk assessment |
| `reason_details` | Reason codes with severity and explanation text |
| `suggested_action` | Action selected by the agent |
| `dashboard_message` | Explanation/action message for the UI |

Risk level distribution from the demo run:

| Risk level | Cart count |
|---|---:|
| Low | 19 |
| Medium | 18 |
| High | 13 |

The distribution is suitable for a demo because it does not label every cart as high risk or every cart as low risk.

---

## 11. Agent policy

The Risk Agent uses explicit policy weights rather than spread-derived weights.

Risk score policy:

| Component | Weight | Rationale |
|---|---:|---|
| Transaction anchor | 0.70 | The transaction model is the only label-backed risk layer. |
| Contextual evidence | 0.30 | Fit, review, and cart signals adjust and explain the risk. |

Contextual evidence policy:

| Component | Weight | Rationale |
|---|---:|---|
| Fit context | 0.45 | Size and fit issues are central to fashion returns. |
| Review context | 0.40 | Review text provides product-specific issue evidence. |
| Cart context | 0.15 | Cart behavior is useful but simulated in the MVP. |

This design avoids letting simulated cart behavior dominate the final risk score.

---

## 12. Diagnostic interpretation

The Risk Agent diagnostics show that the final score remains transaction-anchored while still using contextual evidence.

Expected interpretation:

- The transaction layer provides the main risk direction.
- Fit, review, and cart signals provide context, reasons, and actions.
- The project does not claim that all signal layers have equal predictive power.
- The main value of multi-signal modeling is explainability and intervention selection.

This framing is important for the demo:

```text
Risk ranking is transaction-anchored.
Risk explanation is multi-signal.
Suggested action is reason-driven.
```

---

## 13. Suggested actions

The Risk Agent can return the following action codes:

| Action | Meaning |
|---|---|
| `show_size_guidance_before_checkout` | Show size or fit guidance before checkout |
| `highlight_color_and_product_images` | Highlight product images and color details |
| `show_review_and_product_detail_summary` | Show review summary or product details |
| `confirm_duplicate_variant` | Ask the user to confirm repeated variants |
| `show_return_policy_and_checkout_confirmation` | Show return policy or checkout confirmation |
| `standard_checkout` | Continue with normal checkout |

These actions are selected from reason codes, not only from the numeric risk score. For example, a cart can receive a size guidance action when size-related risk is detected, even if the overall risk level is not high.

---

## 14. What the model can and cannot claim

### The model can support these claims

- The pipeline creates a working end-to-end data/ML flow.
- The baseline model ranks high-risk transactions better than random selection.
- Fit, review, and cart signals provide interpretable risk reasons.
- The Risk Agent produces risk score, risk level, reasons, actions, and messages.
- The project demonstrates an agentic return-prevention decision layer for fashion e-commerce.

### The model should not claim these

- It should not claim production-level return prediction.
- It should not claim proven return reduction or revenue impact.
- It should not claim that UCI products and fashion review items are true matched products.
- It should not treat `risk_score` as a calibrated return probability.
- It should not use agent output as an automatic final decision without human/product constraints.

---

## 15. Final summary

The six-notebook pipeline achieves the MVP data/ML goal of ReturnShield.

It provides:

```text
transaction risk ranking
+ fit/review/cart signals
+ mock cart integration
+ Risk Agent score
+ reason explanation
+ suggested action
+ dashboard message
```

The correct positioning is:

```text
ReturnShield is an agentic decision-support system for pre-checkout return-risk prevention in fashion e-commerce.
It is not only a return prediction model and not only a size recommendation system.
```
