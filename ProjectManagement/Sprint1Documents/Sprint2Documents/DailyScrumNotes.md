BEYZA 

Gün 1
Dün: Sprint 1 tamamlandı, Osman'ın PR'ı incelendi ve merge edildi
Bugün: risk_agent.py (kural tabanlı baseline), signal_agent.py, action_agent.py yazıldı

Gün 2
Dün: Tüm agent sınıfları tamamlandı
Bugün: orchestrator.py yazıldı, /api/agent/analyze-cart ve /api/predict endpoint'leri implement edildi ve Swagger'da test edildi

Gün 3
Dün: Her iki endpoint çalışıyor ve doğrulandı
Bugün: Frontend gerçek API'ye bağlandı, analyzeCart() uçtan uca test edildi ve onaylandı

Gün 4
Dün: Frontend-backend bağlantısı doğrulandı
Bugün: returnshield_agent_cart_scores.csv backend'e entegre edildi (cart_scores.py servisi), pandas requirements'a eklendi
Engel: pandas requirements.txt'te yoktu — Docker rebuild ile çözüldü


Gün 5
Dün: CSV entegrasyonu çalışıyor, CART_0001 gerçek ML verisinden doğru risk skoru döndürüyor
Bugün: /api/dashboard/summary endpoint'i eklendi (gerçek CSV istatistikleri), /api/agent/top-alerts endpoint'i eklendi, /api/orders müşteri adlarını da döndürecek şekilde güncellendi


OSMAN 

Gün 1
Dün: Sprint 1 EDA ve feature engineering tamamlandı
Bugün: Baseline modelleme başladı (Logistic Regression, Random Forest), PR-AUC değerlendirmesi yapıldı

Gün 2
Dün: Baseline modeller eğitildi, metrikler değerlendirildi
Bugün: 04_review_signal_poc.ipynb yazıldı — beden, kalite, renk, olumsuz dil sinyalleri çıkarıldı


Gün 3
Dün: Yorum sinyal notebook'u tamamlandı
Bugün: 05_mock_cart_features.ipynb yazıldı — transaction, fit, yorum sinyalleri sepet seviyesinde birleştirildi


Gün 4
Dün: Mock cart feature'ları hazır
Bugün: 06_returnshield_agent_demo.ipynb yazıldı — risk_score, risk_level, top_reasons, suggested_action, dashboard_message üretildi

Gün 5
Dün: Tam pipeline tamamlandı (01-06 notebook'lar)
Bugün: PR açıldı — tüm notebook'lar, outputs/, data_dictionary.md, dataset_decision.md, model_summary.md, agent_output_schema.md, demo_cart_cases.md, handoff raporu eklendi


TAİBENUR 

Gün 1
Dün: Sprint 1 dashboard tamamlandı
Bugün: index.html'e risk detail modal eklendi, CSS stilleri yazıldı

Gün 2
Dün: Modal yapısı tamamlandı
Bugün: analyzeCart() fonksiyonu gerçek API'ye bağlandı, agent flow görseli ile openDetail() fonksiyonu yazıldı
Engel: Yok

Gün 3
Dün: API bağlantısı uçtan uca çalıştığı doğrulandı
Bugün: cart.html oluşturuldu — risk göstergesi, uyarı kartı, 3 aksiyon butonu (beden rehberi, yorumlar, beden önerisi)

Gün 4
Dün: cart.html tamamlandı ve test edildi
Bugün: CO₂ kartı /api/dashboard/summary'den besleniyor, AI Alerts /api/agent/top-alerts'ten güncellendi, sipariş tablosuna müşteri adları eklendi

Gün 5
Dün: Tüm dinamik veri bağlantıları tamamlandı
Bugün: Sidebar sadeleştirildi (kullanılmayan linkler kaldırıldı), index.html ve api.js İngilizce'ye çevrildi, Sprint2Documents için ekran görüntüleri alındı
