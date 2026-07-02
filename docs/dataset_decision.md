# Dataset Decision

## Document Status

This document summarizes the current dataset decisions for the ReturnShield AI MVP.

Status: **updated after the implementation of notebooks 01-06**

The previous draft separated implemented layers from planned Sprint 1 layers. That is no longer accurate. The following layers are now implemented in the notebook pipeline:

- Online Retail transaction and return/cancel proxy layer
- Baseline transaction risk-ranking model
- ModCloth + RentTheRunway fit signal layer
- Review text and rating signal layer
- Mock cart feature layer
- ReturnShield Risk Agent demo output layer

The current implementation uses a layered data strategy. The datasets are not row-level merged because they do not share the same users, products, sessions, carts, or order IDs.

---

## 1. Purpose

ReturnShield AI is an explainable MVP prototype for identifying possible return-risk signals before checkout in a fashion e-commerce context.

The project does not claim that a single public dataset can fully represent a real production fashion return-prevention system. Instead, it uses a layered data approach:

- transaction and return/cancel proxy signals,
- fashion fit, size, length, and quality signals,
- review-based size, quality, color, rating, and negative-language signals,
- controlled mock cart behavior signals,
- a Risk Agent output layer that produces risk score, risk level, reasons, and suggested actions.

Each data source is used for a specific signal layer. The final demo combines these layers into a controlled MVP cart-level schema.

---

## 2. Current Implementation Status

| Layer | Dataset / Source | Current status | Project usage |
|---|---|---:|---|
| Transaction and return/cancel proxy | UCI Online Retail | Implemented | Main transaction feature layer and proxy label source |
| Baseline risk modeling | UCI Online Retail derived features | Implemented | First baseline risk ranking / transaction model score |
| Fashion fit and size signals | ModCloth + RentTheRunway Clothing Fit Dataset | Implemented | Item-level fit, length, and quality signals |
| Review signal layer | ModCloth + RentTheRunway review text and rating fields | Implemented | Size, quality, color, negative-language, and rating issue signals |
| Mock cart behavior | Controlled simulated demo carts | Implemented | Pre-checkout uncertainty and cart behavior features |
| Risk Agent output | Combined cart-level features | Implemented | Risk score, risk level, reasons, suggested action, and dashboard message |

---

## 3. Core Dataset Decision

The project will not force a single dataset to cover all return-risk factors.

The current decision is:

1. Use UCI Online Retail as the main transaction and return/cancel proxy label dataset.
2. Use ModCloth + RentTheRunway Clothing Fit Dataset for fashion fit, size, length, quality, review text, and rating signals.
3. Use review text already available in the clothing fit datasets instead of introducing a separate unrelated review dataset.
4. Use mock cart simulation for pre-checkout cart behavior because the selected open datasets do not contain real cart-level pre-checkout behavior.
5. Do not perform row-level merging between unrelated datasets.
6. Treat the final `risk_score` as an MVP risk-ranking and decision-support score, not as a calibrated production return probability.

---

## 4. Implemented Dataset 1: UCI Online Retail

### 4.1 Dataset Role

UCI Online Retail is used as the main transaction-level dataset.

In ReturnShield, this dataset is used for:

- transaction data preparation,
- return/cancel proxy label creation,
- transaction-level feature engineering,
- baseline return/cancel risk modeling,
- label-backed risk-ranking input for the Risk Agent.

### 4.2 Why This Dataset Is Used

The dataset contains transaction records from an online retail setting. It includes fields such as invoice number, stock/product code, description, quantity, invoice date, unit price, customer ID, and country.

This makes it suitable for building a transaction-level risk layer.

### 4.3 Return / Cancel Proxy Label

The current project uses a proxy label, not a perfect real-world return label.

The label logic is based on return/cancellation-like transaction behavior available in the dataset, such as cancellation invoice patterns and negative quantity records.

Example logic:

```text
if InvoiceNo indicates cancellation or Quantity < 0:
    is_return = 1
else:
    is_return = 0
```

This label represents return/cancellation-like behavior available from the transaction records.

### 4.4 Important Limitation

UCI Online Retail is not a fashion-specific dataset. Therefore, it should not be used to claim that the model directly learns fashion-specific return reasons such as size mismatch, color mismatch, or fabric quality issues.

In this project, UCI Online Retail is used only for the transaction and return/cancel proxy layer.

### 4.5 Current Notebook Usage

Implemented notebooks using this layer:

```text
notebooks/01_online_retail_data_preparation.ipynb
notebooks/02_online_retail_baseline_modeling.ipynb
```

Local pipeline outputs:

```text
data/processed/online_retail_eda_features.csv
data/processed/online_retail_model_base.csv
data/processed/online_retail_test_scores.csv
```

Tracked output artifacts:

```text
outputs/01_online_retail_data_preparation/
outputs/02_online_retail_baseline_modeling/
```

---

## 5. Implemented Dataset 2: ModCloth + RentTheRunway Clothing Fit Dataset

### 5.1 Dataset Role

The Clothing Fit layer is used to generate fashion-specific fit, length, quality, review, and rating signals.

It is not used as the main return label source.

### 5.2 Why This Dataset Is Used

ReturnShield needs fashion-specific risk signals that cannot be derived from UCI Online Retail. The Clothing Fit datasets provide user feedback from fashion platforms.

This layer supports signals such as:

- fit mismatch,
- too small / too large tendency,
- length issue,
- quality issue,
- review text size issue,
- review text quality issue,
- review text color issue,
- negative-language signal,
- rating issue signal.

### 5.3 Current Signal Logic

Example fit logic:

```text
if fit is "small" or "large":
    fit_issue = 1

if fit is "fit":
    fit_issue = 0
```

Example review logic:

```text
review text -> keyword-based issue counts -> item-level smoothed issue scores
```

The current MVP uses interpretable signal extraction rather than a large black-box NLP model.

### 5.4 Current Notebook Usage

Implemented notebooks:

```text
notebooks/03_fit_signal_poc.ipynb
notebooks/04_review_signal_poc.ipynb
```

Local pipeline outputs:

```text
data/processed/fit_signals.csv
data/processed/review_signals.csv
data/processed/review_signal_handoff.csv
```

Tracked output artifacts:

```text
outputs/03_fit_signal_poc/
outputs/04_review_signal_poc/
```

### 5.5 Important Limitation

The Clothing Fit dataset users are not the same users as the UCI Online Retail customers.

The project does not assume that a UCI customer and a ModCloth or RentTheRunway reviewer are the same person.

The output is used as an item-level auxiliary signal layer, not as a row-level extension of UCI transactions.

---

## 6. Implemented Layer: Review Signal PoC

### 6.1 Current Status

The review signal layer is now implemented.

Implemented notebook:

```text
notebooks/04_review_signal_poc.ipynb
```

Local pipeline outputs:

```text
data/processed/review_signals.csv
data/processed/review_signal_handoff.csv
```

Tracked diagnostic output:

```text
outputs/04_review_signal_poc/review_signal_diagnostics.csv
```

### 6.2 Purpose

The review layer extracts text-based risk signals related to:

- size issues,
- quality issues,
- color issues,
- negative language,
- rating-based dissatisfaction.

### 6.3 Current Signal Fields

Important output fields include:

```text
review_text_size_issue_score
review_text_quality_issue_score
review_text_color_issue_score
review_text_negative_language_score
rating_issue_score
review_text_reliability_weight
rating_signal_reliability_weight
top_review_text_issue
review_text_color_issue_score_upper_tail_flag
```

### 6.4 Important Limitation

The review layer is an MVP signal extraction layer. It should not be presented as a production-grade sentiment analysis or LLM-based review understanding system.

The current implementation is interpretable and suitable for prototype explanation, but it does not prove causal return reduction.

---

## 7. Implemented Layer: Mock Cart Features

### 7.1 Current Status

The mock cart feature layer is now implemented.

Implemented notebook:

```text
notebooks/05_mock_cart_features.ipynb
```

Local pipeline outputs:

```text
data/processed/mock_cart_features.csv
data/processed/mock_cart_items.csv
```

Tracked output artifacts:

```text
outputs/05_mock_cart_features/mock_cart_feature_diagnostics.csv
outputs/05_mock_cart_features/mock_cart_simulation_config.csv
outputs/05_mock_cart_features/mock_product_signal_map.csv
```

### 7.2 Purpose

The mock cart layer creates a cart-level demo input table for the Risk Agent and dashboard.

The selected public datasets do not contain real pre-checkout cart behavior. Therefore, cart behavior is simulated for MVP demonstration purposes.

### 7.3 Simulated Fields

Implemented simulated/demo fields include:

```text
cart_id
mock_user_id
primary_mock_product_id
primary_source_item_id
cart_item_count
unique_mock_product_count
two_size_same_product
duplicate_variant
cart_uncertainty_signal_count
cart_size_pressure
```

### 7.4 Combined Risk Agent Input

The mock cart feature table combines transaction, fit, review, and cart behavior layers into a common schema.

Important final input fields include:

```text
model_risk_rank_score
model_risk_score_raw
night_purchase
fit_layer_summary_score
item_fit_issue_score
item_length_issue_score
item_quality_issue_score
review_text_summary_score
review_text_size_issue_score
review_text_quality_issue_score
review_text_color_issue_score
review_text_negative_language_score
rating_issue_score
fit_signal_available
review_signal_available
rating_signal_available
```

### 7.5 Important Limitation

Mock cart rows are simulated demo records. They should be clearly marked as simulated in the data dictionary and should not be presented as real production cart traffic.

Notebook 05 creates Risk Agent input features only. It does not create the final `risk_score`, `risk_level`, or final action output. Those are produced in Notebook 06.

---

## 8. Implemented Layer: Risk Agent Demo Output

### 8.1 Current Status

The Risk Agent demo layer is implemented.

Implemented notebook:

```text
notebooks/06_returnshield_agent_demo.ipynb
```

Tracked output artifacts:

```text
outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
outputs/06_returnshield_agent_demo/returnshield_agent_config.csv
outputs/06_returnshield_agent_demo/returnshield_agent_diagnostics.csv
outputs/06_returnshield_agent_demo/returnshield_agent_summary.csv
```

### 8.2 Purpose

This layer converts the cart-level input table into an explainable demo output for backend/frontend use.

It produces:

```text
risk_score
risk_percentile_rank
risk_level
label_backed_risk_score
contextual_evidence_score
top_reasons
reason_details
suggested_action
dashboard_message
```

### 8.3 Current Risk Scoring Design

The final score is transaction-anchored and context-aware.

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

### 8.4 Important Limitation

The final `risk_score` is not a calibrated probability of return. It is a risk-ranking and decision-support score for the MVP demo.

---

## 9. Why Row-Level Merging Is Not Used

The datasets do not share common identifiers.

There is no reliable key connecting:

- a UCI Online Retail customer,
- a ModCloth user,
- a RentTheRunway user,
- a fashion review item,
- a simulated cart user,
- a real cart or session.

Therefore, row-level merging would create artificial and misleading relationships.

ReturnShield uses the following layered approach:

```text
UCI Online Retail -> transaction and return/cancel proxy signal
Clothing Fit Dataset -> fit, size, length, quality, review, and rating signals
Mock cart simulation -> pre-checkout cart uncertainty signal
Risk Agent demo -> risk score, reasons, suggested actions, and dashboard message
```

These layers are mapped into a shared feature schema for the MVP demo, but the project does not claim that they come from the same real users or orders.

---

## 10. Data Status Definitions

The project labels each field using one of the following statuses:

| Status | Meaning |
|---|---|
| real | Directly available in a source dataset |
| derived | Computed from real fields |
| simulated | Created for controlled MVP demonstration |
| model_output | Produced by a model or scoring function |
| agent_output | Produced by an agent layer |
| diagnostic | Produced for evaluation, audit, or explanation |

Examples:

| Field | Status | Explanation |
|---|---|---|
| `InvoiceNo` | real | Directly available in UCI Online Retail |
| `is_return` | derived | Created from invoice/quantity logic |
| `selected_model_score` | model_output | Produced by baseline modeling |
| `model_risk_rank_score` | model_output / derived | Percentile/rank version of model score |
| `item_fit_issue_score` | derived | Aggregated from Clothing Fit feedback |
| `review_text_size_issue_score` | derived | Extracted from review text |
| `two_size_same_product` | simulated | Created in mock cart simulation |
| `risk_score` | agent_output | Produced in Notebook 06 |
| `risk_level` | agent_output | Produced in Notebook 06 |
| `suggested_action` | agent_output | Produced in Notebook 06 |
| `dashboard_message` | agent_output | Produced in Notebook 06 |

---

## 11. Raw Data and Generated Output Policy

Raw datasets are not committed to Git.

Processed local pipeline tables are not committed to Git.

Tracked repository artifacts include:

- source code,
- notebooks,
- documentation,
- selected output plots,
- selected output metrics,
- selected diagnostics and summaries under `outputs/`.

The following folders remain excluded through `.gitignore`:

```text
data/raw/
data/processed/
```

The `outputs/` folder is tracked because it contains lightweight notebook artifacts used as evidence for review, demo, and team handoff.

---

## 12. Out of Scope for the Current MVP

The following items are out of scope for the current MVP:

- image-based product analysis,
- DeepFashion2,
- product photo comparison,
- virtual try-on,
- real payment system integration,
- real company integration,
- real customer personal data,
- production-level return reduction proof,
- calibrated production return probability,
- true row-level matching between UCI transactions and fashion review products.

These can be mentioned as future improvements, but they should not be presented as implemented functionality.

---

## 13. Key Limitations

The current MVP has the following limitations:

1. UCI Online Retail is not a fashion-specific dataset.
2. The return/cancel label is a proxy, not a perfect real-world return label.
3. Clothing Fit data is used for auxiliary fashion signals, not for direct return labels.
4. Review signals are extracted from available fashion review text and rating fields, not from a separate production review system.
5. Mock cart behavior is simulated.
6. The datasets are not row-level merged.
7. The model score should be interpreted as a risk-ranking signal, not a definitive return probability.
8. The project does not claim to prove real return reduction.
9. The Risk Agent output is a controlled decision-support output, not an autonomous purchase decision.

---

## 14. References

- UCI Machine Learning Repository: Online Retail Dataset  
  https://archive.ics.uci.edu/dataset/352/online+retail

- UCSD / McAuley Lab: Clothing Fit Datasets  
  https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit

---

## 15. Summary

ReturnShield AI uses a layered data strategy because no single public dataset covers all required signals for pre-checkout return-risk analysis.

The current implemented pipeline provides:

- transaction-based return/cancel proxy features,
- baseline transaction risk scoring,
- fashion fit, length, quality, review, and rating signals,
- controlled mock cart behavior features,
- a common Risk Agent input table,
- final Risk Agent outputs for backend/frontend handoff.

The main handoff output is:

```text
outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
```

This output provides one row per demo cart with:

```text
risk_score
risk_level
top_reasons
reason_details
suggested_action
dashboard_message
```
