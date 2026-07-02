# Dataset Decision Draft

## Document Status

This document summarizes the Sprint 1 dataset decisions for ReturnShield AI.

It separates implemented data layers from planned data layers. The current project pipeline has implemented the Online Retail and Clothing Fit layers. The standalone review signal layer and mock cart feature layer are still planned Sprint 1 completion tasks.

This document should be updated after the review signal and mock cart notebooks are implemented.

---

## 1. Purpose

ReturnShield AI is an explainable MVP prototype for identifying possible return-risk signals before checkout in an e-commerce context.

The project does not claim that a single public dataset can fully represent a real production fashion return-prevention system. Instead, the project uses a layered data approach:

- transaction and return/cancel proxy signals,
- fashion fit and size mismatch signals,
- review-based quality, size, and color issue signals,
- simulated cart behavior signals.

Each data source is used for a specific signal layer. The datasets are not row-level merged because they do not contain the same users, products, sessions, carts, or order IDs.

---

## 2. Current Implementation Status

| Layer | Dataset / Source | Current Status | Project Usage |
|---|---|---:|---|
| Transaction and return/cancel proxy | UCI Online Retail | Implemented | Main transaction feature layer and proxy label source |
| Baseline risk modeling | UCI Online Retail derived features | Implemented | First baseline risk ranking / model score |
| Fashion fit and size signals | ModCloth + RentTheRunway Clothing Fit Dataset | Implemented | Item-level fit, length, quality, and review keyword signals |
| Standalone review signal layer | Review dataset or review text layer | Planned | Quality, color, size, and sentiment signals |
| Mock cart behavior | Simulated demo data | Planned | Pre-checkout uncertainty and cart behavior features |

---

## 3. Core Dataset Decision

The project will not force a single dataset to cover all return-risk factors.

The current decision is:

1. Use UCI Online Retail as the main transaction and return/cancel proxy label dataset.
2. Use ModCloth + RentTheRunway Clothing Fit Dataset for fashion fit, size, length, and quality mismatch signals.
3. Add a review signal layer only as an auxiliary signal source. This layer is planned and should not be described as completed until the notebook is implemented.
4. Use mock cart simulation for pre-checkout cart behavior because the selected open datasets do not contain real cart-level pre-checkout behavior.
5. Do not perform row-level merging between unrelated datasets.

---

## 4. Implemented Dataset 1: UCI Online Retail

### 4.1 Dataset Role

UCI Online Retail is used as the main transaction-level dataset.

In ReturnShield, this dataset is used for:

- transaction data preparation,
- return/cancel proxy label creation,
- transaction-level feature engineering,
- baseline return/cancel risk modeling.

### 4.2 Why This Dataset Is Used

The dataset contains transaction records from an online retail setting. It includes fields such as invoice number, stock/product code, description, quantity, invoice date, unit price, customer ID, and country.

This makes it suitable for building a transaction-level risk layer.

### 4.3 Return / Cancel Proxy Label

The current project uses a proxy label, not a perfect real-world return label.

The label logic is:

```text
if InvoiceNo starts with "C" or Quantity < 0:
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

Expected local outputs:

```text
data/processed/online_retail_eda_features.csv
data/processed/online_retail_model_base.csv
outputs/online_retail_modeling_metrics.csv
outputs/online_retail_top_k_lift.csv
outputs/online_retail_test_scores.csv
```

Generated outputs are not tracked by Git.

---

## 5. Implemented Dataset 2: ModCloth + RentTheRunway Clothing Fit Dataset

### 5.1 Dataset Role

The Clothing Fit layer is used to generate fashion-specific fit and size mismatch signals.

It is not used as the main return label source.

### 5.2 Why This Dataset Is Used

ReturnShield needs fashion-specific risk signals that cannot be derived from UCI Online Retail. The Clothing Fit dataset provides fit-related feedback from fashion platforms.

This layer supports signals such as:

- fit mismatch,
- too small / too large tendency,
- length issue,
- quality issue,
- review keyword signals when review text is available.

### 5.3 Current Signal Logic

Example logic:

```text
if fit is "small" or "large":
    fit_issue = 1

if fit is "fit":
    fit_issue = 0
```

Item-level signals are then generated from row-level feedback.

### 5.4 Current Notebook Usage

Implemented notebook:

```text
notebooks/03_fit_signal_poc.ipynb
```

Expected local output:

```text
data/processed/fit_signals.csv
```

### 5.5 Important Limitation

The Clothing Fit dataset users are not the same users as the UCI Online Retail customers.

The project does not assume that a UCI customer and a ModCloth or RentTheRunway reviewer are the same person.

The output is used as an item-level auxiliary signal layer, not as a row-level extension of UCI transactions.

---

## 6. Planned Layer: Standalone Review Signal PoC

### 6.1 Current Status

This layer is planned but not yet fully implemented as a separate notebook.

A separate notebook is expected:

```text
notebooks/04_review_signal_poc.ipynb
```

Expected local output:

```text
data/processed/review_signals.csv
```

### 6.2 Purpose

The review layer will extract text-based risk signals related to:

- size issues,
- quality issues,
- color issues,
- general sentiment.

### 6.3 Candidate Signal Logic

The first Sprint 1 version can be keyword-based. It does not need to be a production-level NLP model.

Example keyword groups:

```text
Size issue keywords:
small, tight, too small, large, too big, size up, size down

Quality issue keywords:
cheap, thin, poor quality, bad fabric, ripped, low quality

Color issue keywords:
different color, not as pictured, color is different, faded
```

Possible output fields:

```text
product_id
review_count
avg_rating
review_size_signal_rate
quality_issue_score
color_issue_score
sentiment_score
review_signal_reliability
```

### 6.4 Important Limitation

Until this notebook is implemented, the review layer should be described as planned, not completed.

The project should not claim that a standalone review dataset has already been fully integrated.

---

## 7. Planned Layer: Mock Cart Features

### 7.1 Current Status

This layer is planned but not yet implemented.

A separate notebook is expected:

```text
notebooks/05_mock_cart_features.ipynb
```

Expected local output:

```text
data/processed/mock_cart_features.csv
```

### 7.2 Purpose

The mock cart layer will create a demo input table for the Risk Agent and dashboard.

The selected public datasets do not contain real pre-checkout cart behavior. Therefore, cart behavior will be simulated for MVP demonstration purposes.

### 7.3 Planned Simulated Fields

Example simulated fields:

```text
cart_id
mock_user_id
mock_product_id
two_size_same_product
duplicate_variant
cart_item_count
cart_uncertainty_score
```

Example logic:

```text
if the same product appears in two different sizes in the cart:
    two_size_same_product = 1
    cart_uncertainty_score increases
```

### 7.4 Combined Risk Agent Input

The mock cart feature table will combine signal layers into a common schema for demonstration.

Example fields:

```text
cart_id
mock_user_id
mock_product_id
unit_price
night_purchase
customer_return_rate
product_return_rate
model_risk_score
item_fit_issue_score
item_length_issue_score
item_quality_issue_score
review_size_signal_rate
quality_issue_score
color_issue_score
two_size_same_product
duplicate_variant
cart_uncertainty_score
risk_score
risk_level
top_reasons
```

### 7.5 Important Limitation

Mock cart rows are simulated demo records. They should be clearly marked as simulated in the data dictionary.

---

## 8. Why Row-Level Merging Is Not Used

The datasets do not share common identifiers.

There is no reliable key connecting:

- a UCI Online Retail customer,
- a ModCloth user,
- a RentTheRunway user,
- a review dataset user,
- a simulated cart user.

Therefore, row-level merging would create artificial and misleading relationships.

ReturnShield uses the following layered approach:

```text
UCI Online Retail -> transaction and return/cancel proxy signal
Clothing Fit Dataset -> fit and size mismatch signal
Review layer -> text-based issue signal
Mock cart simulation -> pre-checkout cart uncertainty signal
```

These layers are mapped into a shared feature schema for the MVP demo, but the project does not claim that they come from the same real users or orders.

---

## 9. Data Status Definitions

The project should label each field using one of the following statuses:

| Status | Meaning |
|---|---|
| real | Directly available in a source dataset |
| derived | Computed from real fields |
| simulated | Created for controlled MVP demonstration |
| model_output | Produced by a model or scoring function |
| agent_output | Produced by an agent layer |

Examples:

| Field | Status | Explanation |
|---|---|---|
| InvoiceNo | real | Directly available in UCI Online Retail |
| is_return | derived | Created from InvoiceNo and Quantity |
| customer_return_rate | derived | Computed from transaction history |
| model_risk_score | model_output | Produced by baseline modeling |
| item_fit_issue_score | derived | Aggregated from Clothing Fit feedback |
| two_size_same_product | simulated | Created in mock cart simulation |
| risk_level | agent_output / model_output | Produced by the risk scoring layer |

---

## 10. Raw Data and Generated Output Policy

Raw datasets are not committed to Git.

Generated outputs are also not committed to Git.

The repository keeps only:

- source code,
- notebooks,
- documentation,
- configuration files.

The following folders are excluded through `.gitignore`:

```text
data/raw/
data/processed/
outputs/
```

This keeps the repository small and avoids treating generated files as source files.

---

## 11. Out of Scope for Sprint 1

The following items are out of scope for Sprint 1:

- image-based product analysis,
- DeepFashion2,
- product photo comparison,
- virtual try-on,
- real payment system integration,
- real company integration,
- real customer personal data,
- production-level return reduction proof.

These can be mentioned as future improvements, but they should not be presented as implemented Sprint 1 functionality.

---

## 12. Key Limitations

The current MVP has the following limitations:

1. UCI Online Retail is not a fashion-specific dataset.
2. The return/cancel label is a proxy, not a perfect real-world return label.
3. Clothing Fit data is used for auxiliary fit signals, not for direct return labels.
4. The standalone review layer is still planned.
5. Mock cart behavior is simulated.
6. The datasets are not row-level merged.
7. The model score should be interpreted as a risk ranking signal, not a definitive return probability.
8. The project does not claim to prove real return reduction.

---

## 13. References

- UCI Machine Learning Repository: Online Retail Dataset  
  https://archive.ics.uci.edu/dataset/352/online+retail

- UCSD / McAuley Lab: Clothing Fit Datasets  
  https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit

---

## 14. Summary

ReturnShield AI uses a layered data strategy because no single public dataset covers all required signals for pre-checkout return-risk analysis.

The current implemented layers provide:

- transaction-based return/cancel proxy features,
- baseline risk scoring,
- fashion fit and quality-related item signals.

The planned Sprint 1 completion layers will add:

- standalone review-based issue signals,
- mock cart behavior features,
- a common Risk Agent input table.
