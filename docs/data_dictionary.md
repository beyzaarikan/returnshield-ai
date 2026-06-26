# ReturnShield AI — Veri Sözlüğü

## Veri Kaynakları
| Kaynak | Açıklama |
|--------|----------|
| Online Retail (UC Irvine) | Gerçek e-ticaret işlem verisi |
| Simüle sepet datası | Kontrollü üretilmiş demo verisi |
| Örnek yorumlar | PoC için hazırlanmış örnek Türkçe yorumlar |

## Alan Açıklamaları
| Alan | Açıklama | Kaynak | Durum |
|------|----------|--------|-------|
| InvoiceNo | Sipariş numarası | Online Retail | Gerçek |
| Quantity | Ürün miktarı | Online Retail | Gerçek |
| UnitPrice | Ürün fiyatı | Online Retail | Gerçek |
| CustomerID | Anonim müşteri ID | Online Retail | Gerçek/anonim |
| is_return | Quantity < 0 ise 1 | Türetilmiş | Gerçek veriden türetilmiş |
| night_purchase | 22:00-02:00 arası mı? | Türetilmiş | Türetilmiş |
| two_size_same_product | Aynı ürün 2 beden sepette | Simüle | Simüle |
| size_issue_score | Yorum beden şikayeti skoru | Yorum analizi PoC | PoC/türetilmiş |
| customer_return_count | Müşteri geçmiş iade sayısı | Türetilmiş | Türetilmiş |

## Önemli Not
Bu MVP'de gerçek ve simüle veri karışık kullanılmaktadır.
Hangi alanın gerçek, hangisinin simüle olduğu yukarıdaki tabloda açıkça belirtilmiştir.
Sonuçlar "kanıtlanmış iade azaltımı" olarak değil, çalışan bir prototip olarak sunulmalıdır.