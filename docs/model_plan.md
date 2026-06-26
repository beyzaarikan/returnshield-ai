# ReturnShield AI — Model Planı

## Yaklaşım
Kademeli modelleme: önce kural tabanlı baseline, sonra ML modeli.

## Aşamalar

### Baseline (Sprint 1)
Kural tabanlı ağırlıklı skor:
- Gece alışverişi → +0.2
- Aynı üründen 2 beden → +0.3
- Tekrar iade geçmişi → +0.2
- Yorum beden şikayeti → +0.2

### ML Model (Sprint 2)
XGBoost veya LightGBM:
- Sprint 1'de çıkarılan feature'lar kullanılır
- Cross-validation ile eğitilir
- model.pkl olarak export edilir

## Feature Listesi
| Feature | Açıklama | Kaynak |
|---------|----------|--------|
| order_hour | Sipariş saati | Gerçek |
| night_purchase | 22:00-02:00 arası mı? | Türetilmiş |
| customer_return_count | Geçmiş iade sayısı | Türetilmiş |
| two_size_same_product | 2 beden sepette mi? | Simüle |
| size_issue_score | Yorum beden şikayeti skoru | Yorum analizi |
| color_issue_score | Yorum renk şikayeti skoru | Yorum analizi |
| unit_price | Ürün fiyatı | Gerçek |

## Değerlendirme Metrikleri
- Precision, Recall, F1-score
- Confusion matrix
- SHAP feature importance

## Önemli Not
Bu MVP gerçek üretim modeli değil, çalışan bir karar destek prototipidir.
Açık veri + simüle veri ayrımı data_dictionary.md'de belgelenmiştir.