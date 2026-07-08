## Ürün İsmi
ReturnShield AI

## Takım İsmi
Grup 77

## Takım Üyeleri

| Kişi | Rol |
|------|-----|
|Beyza Şefika Arıkan | Backend + AI Lead |
|Taibenur Yavuz | Frontend |
|Osman Şahan | Data / ML |

# Ürün İle İlgili Bilgiler

#Ürün Açıklaması
ReturnShield AI, moda e-ticaretinde satın alma öncesi iade riskini tespit eden agentic AI tabanlı bir karar destek sistemidir. Sepet davranışı, ürün yorumları ve müşteri geçmişini analiz ederek risk skoru üretir, riskin nedenini açıklar ve hem müşteriye hem işletmeye doğru aksiyonu önerir.

## Ürün Özellikleri
Sepet analizi: aynı üründen birden fazla beden, gece alışverişi gibi davranışsal sinyaller
Yorum analizinden beden/renk/kalite şikayeti tespiti
ML destekli risk skoru (XGBoost/Random Forest)
Agentic AI mimarisi: Orchestrator, Signal, Risk, Action agent'ları
Müşteri ekranında yumuşak, manipülatif olmayan uyarı mesajı
İşletme dashboard'unda riskli sipariş listesi ve aksiyon önerileri
Sürdürülebilirlik farkındalığı (önlenen iade ile CO₂/kargo tasarrufu)

## Hedef Kitle
Moda/tekstil/ayakkabı kategorisinde satış yapan e-ticaret işletmeleri ve bu platformlardan alışveriş yapan online müşteriler. İşletme tarafında kategori yöneticileri ve müşteri destek ekipleri; müşteri tarafında satın alma kararı verirken emin olamayan kullanıcılar.

# Sprint 1

*Backlog Düzeni ve Story Seçimleri*
Backlog, ilk yapılacak görevlere göre önceliklendirilmiştir. Her sprint için tahmin edilen puan sınırını aşmayacak şekilde sıradan seçimler yapılmaktadır. Görevler backend, frontend ve data/ML olmak üzere üç ana sorumluluk alanına bölünmüş, her alan kendi içinde bağımsız çalışabilecek şekilde tasarlanmıştır.

GitHub Projects board'unda kartlar Backlog → Sprint 1 → In Progress  → Done kolonlarında takip edilmektedir. Her kart bir görevi temsil eder ve ilgili kişiye atanmıştır.
https://github.com/users/beyzaarikan/projects/2/views/1?layout=board

<img width="1311" height="866" alt="Ekran görüntüsü 2026-07-03 180539" src="https://github.com/user-attachments/assets/1358bb4a-98e9-4cf1-ad6b-4816b559b9f6" />
<img width="1289" height="818" alt="image" src="https://github.com/user-attachments/assets/7c5cfa49-11d6-4a27-8c77-a3f4eb24eaa2" />


## *Daily Scrum*
Daily Scrum toplantıları zamansal sebeplerden ötürü WhatsApp üzerinden yazılı olarak yapılmaktadır. Notlar [ProjectManagement/SprintXDocuments/DailyScrumNotes.md](https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint1Documents/DailyScrumNotes.md) dosyasında tutulur.

## *Sprint 1 Review'da alınan kararlar:*

Her sprint sonunda tamamlanan görevler ve çalışan ürün ekran görüntüleri ile birlikte gözden geçirilir. Sprint Review notları [ProjectManagement/SprintXDocuments/SprintReview.md](https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint1Documents/SprintReview.md) dosyasında, acceptance criteria'ların karşılanıp karşılanmadığı kontrol edilerek tutulur.

Backend, Docker Compose üzerinden PostgreSQL ile çalışacak şekilde kuruldu; bu karar geliştirme ortamının tüm takım üyeleri için tutarlı olmasını sağlamıştır.
Frontend için React yerine HTML+Tailwind tercih edilmiştir; gerekçe, takım üyelerinin tamamında Node.js kurulu olmaması ve sprint süresinin kısıtlı olmasıdır.
Agentic AI mimarisi (Orchestrator, Signal, Risk, Action) için Sprint 1'de yalnızca klasör iskeleti oluşturulmuş, implementasyon Sprint 2'ye bırakılmıştır.
Çıkan ürünün (Swagger API, dashboard) çalışmasında bir problem görülmemiştir.

## *Sprint Retrospective'de alınan kararlar*

Sprint Retrospective notları[ ProjectManagement/SprintXDocuments/Retrospective.md](https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint1Documents/Retrospective.md) dosyasında tutulur.

Data/ML tarafında çalışmanın notebook üzerinde ilerlerken düzenli aralıklarla GitHub'a push edilmesi gerektiği görülmüştür; bundan sonra her gün sonunda küçük commit'ler atılacaktır.
Backend tarafında klasör yapısı (iç içe geçmiş dizinler) erken aşamada düzeltilmiş, bu tür yapısal sorunların sprint başında kontrol edilmesi kararlaştırılmıştır.
Sprint 2'de agent entegrasyonu ve model bağlantısı için backend-data/ML arasındaki feature sırası/isimlendirme uyumunun önceden netleştirilmesi gerektiği görülmüştür.

*Ürün Durumu: Ekran görüntüleri:
<img width="1368" height="737" alt="productss1" src="https://github.com/user-attachments/assets/fc5007eb-d7f2-449a-a4d2-926013596e40" />
<img width="474" height="410" alt="products2" src="https://github.com/user-attachments/assets/e55d998c-10a3-4756-bb28-4c36060086f1" />


# Sprint 2

GitHub Projects board'unda kartlar Backlog → Sprint 1 → to-do → In Progress  → Done kolonlarında takip edilmektedir. Her kart bir görevi temsil eder ve ilgili kişiye atanmıştır.

https://github.com/users/beyzaarikan/projects/2/views/1?layout=board

<img width="1656" height="803" alt="Ekran görüntüsü 2026-07-08 203613" src="https://github.com/user-attachments/assets/a7f87e79-7e30-4711-90e9-add1dbd68943" />
<img width="1546" height="833" alt="Ekran görüntüsü 2026-07-08 203636" src="https://github.com/user-attachments/assets/c9125298-327e-4a03-8e46-bde60e9c74ae" />
<img width="1474" height="844" alt="Ekran görüntüsü 2026-07-08 203711" src="https://github.com/user-attachments/assets/ca0f21e0-788b-4135-8a94-0f95b63a85a2" />

## *Daily Scrum*
Daily Scrum toplantıları zamansal sebeplerden ötürü WhatsApp üzerinden yazılı olarak yapılmaktadır. Notlar https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint2Documents/DailyScrumNotes.md dosyasında tutulur.

## *Sprint 2 Review'da alınan kararlar:*

Her sprint sonunda tamamlanan görevler ve çalışan ürün ekran görüntüleri ile birlikte gözden geçirilir. Sprint Review notları https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint2Documents/SprintReview.md dosyasında, acceptance criteria'ların karşılanıp karşılanmadığı kontrol edilerek tutulur.

 /api/predict ve /api/agent/analyze-cart endpoint'leri çalışıyor
 ML modeli veya risk motoru API'den çağrılıyor, response şeması frontend ile uyumlu
 Risk nedenleri ve AI mesajı ekranda gösteriliyor
 Precision/Recall/F1 raporu, model dosyası ve açıklanabilirlik grafiği hazır (outputs/ klasöründe)
 analyze-cart response içinde agents_used, reasons, customer_message, merchant_action dönüyor

## *Sprint Retrospective'de alınan kararlar*

Sprint Retrospective notları https://github.com/beyzaarikan/returnshield-ai/blob/main/ProjectManagement/Sprint1Documents/Sprint2Documents/Retrospective.md dosyasında tutulur.

Sprint 3'te demo akışı baştan sona prova edilecek — video çekiminden önce tüm ekip aynı anda test edecek
README kurulum adımları Sprint 3'te netleştirilecek — tek komutla çalışır hale getirilecek
AI Alerts'teki cart_id isimleri daha okunabilir hale getirilecek

*Ürün Durumu: Ekran görüntüleri:

<img width="1600" height="763" alt="image" src="https://github.com/user-attachments/assets/f23f1820-d342-43a5-a8fe-879dac9d9a0d" />
<img width="489" height="724" alt="image" src="https://github.com/user-attachments/assets/d97f116e-46e2-4de4-a33d-f575e69feee2" />
<img width="386" height="371" alt="image" src="https://github.com/user-attachments/assets/6786b3c8-afe2-4e92-ad0d-6a00b5aa544a" />


# Sprint 3

Final entegrasyon, demo senaryosu, sunum hazırlığı yapılacak


### Gereksinimler

## Backend'i Çalıştırma 

Docker Desktop açıkken proje kökünde:

```bash
docker compose up
 `http://localhost:8000/docs`

---

## Frontend'i Çalıştırma
Canlı önizleme için (opsiyonel):

```bash
# Python varsa:
python -m http.server 3000

# Node varsa:
npx serve .
```
Sonra `http://localhost:3000` aç.

---

## Data / ML Çalıştırma

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook
```



