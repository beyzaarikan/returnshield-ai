# ReturnShield AI — Proje Kapsamı

## Tek cümlelik tanım
Moda e-ticaretinde sepet aşamasındaki iade riskini yorum analizi, kullanıcı/sepet davranışı ve ML modeliyle hesaplayan; risk nedenlerini açıklayan ve kullanıcı/işletme için iade önleyici aksiyon öneren agentic AI sistemidir.

## Problem
E-ticarette iadeler satış sonrası ele alınır. ReturnShield satın alma öncesinde riskli sepeti tespit eder, nedenini açıklar ve müdahale önerir.

## Çözüm
- Sepet davranışı analizi (gece alışverişi, aynı üründen 2 beden)
- Ürün yorumlarından sinyal çıkarma (beden, renk, kumaş şikayetleri)
- Müşteri geçmişi (tekrar iade davranışı)
- ML risk skoru + LLM destekli açıklama

## MVP Kapsamı
- Moda/tekstil/ayakkabı kategorisi
- Simüle + açık veri ile çalışan demo
- Müşteri sepet uyarı ekranı
- İşletme risk dashboard'u
- Agentic AI akışı: Orchestrator → Signal → Risk → Action

## Kapsam Dışı
- Gerçek ödeme sistemi
- Üretim ortamı güvenlik sertifikasyonu
- Tüm e-ticaret kategorileri