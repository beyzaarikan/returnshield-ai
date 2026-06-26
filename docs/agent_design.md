# ReturnShield AI — Agent Tasarımı

## Mimari Özet
Orchestrator Agent süreci yönetir. Diğer agentlar sırayla çalışır ve çıktılarını birbirine aktarır.

## Agent Rolleri

### Orchestrator Agent
- Sepet olayını alır
- Hangi agentların çalışacağını belirler
- Sonuçları birleştirip frontend'e döner

### Signal Agent
- Ürün yorumlarından sinyal çıkarır (beden, renk, kumaş)
- Sepet davranışını analiz eder (gece alışverişi, duplicate beden)
- Müşteri geçmişini okur (tekrar iade sayısı)
- Çıktı: feature/sinyal sözlüğü

### Risk Agent
- Signal Agent çıktısını alır
- ML modeli ile risk skoru hesaplar
- Çıktı: risk_score (0-1), risk_level (low/mid/high), top_factors

### Action Agent
- Risk nedenlerine göre müdahale seçer
- Müşteriye yumuşak uyarı metni üretir (LLM destekli)
- İşletmeye aksiyon önerisi üretir
- Çıktı: customer_message, merchant_action

## Örnek Çıktı
```json
{
  "risk_score": 0.84,
  "risk_level": "high",
  "agents_used": ["SignalAgent", "RiskAgent", "ActionAgent"],
  "reasons": [
    "Yorumlarda beden uyumsuzluğu sinyali yüksek",
    "Aynı ürün iki farklı bedenle sepete eklendi",
    "Sipariş gece saatinde oluşturuldu"
  ],
  "customer_message": "Bu ürün bazı kullanıcılara dar gelmiş. Beden rehberini kontrol etmek ister misiniz?",
  "merchant_action": "Ürün açıklamasına kalıp bilgisi eklenmeli, beden rehberi öne çıkarılmalı."
}
```

## Sprint Planı
- Sprint 1: Klasör yapısı + boş agent dosyaları
- Sprint 2: Agent implementasyonu + /api/agent/analyze-cart endpoint
- Sprint 3: Demo senaryosu + final entegrasyon