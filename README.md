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

 ### Sprint Board Update Screenshots

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

 ### Sprint Board Update Screenshots
 
<img width="1656" height="803" alt="Ekran görüntüsü 2026-07-08 203613" src="https://github.com/user-attachments/assets/a7f87e79-7e30-4711-90e9-add1dbd68943" />
<img width="1546" height="833" alt="Ekran görüntüsü 2026-07-08 203636" src="https://github.com/user-attachments/assets/c9125298-327e-4a03-8e46-bde60e9c74ae" />
<img width="1474" height="844" alt="Ekran görüntüsü 2026-07-08 203711" src="https://github.com/user-attachments/assets/ca0f21e0-788b-4135-8a94-0f95b63a85a2" />

## *Daily Scrum*
Daily Scrum toplantıları zamansal sebeplerden ötürü WhatsApp üzerinden yazılı olarak da yapılmaktadır.
<img width="932" height="646" alt="image" src="https://github.com/user-attachments/assets/98bd3ab9-50b5-4f88-bfc7-77f4a088345a" />
<img width="914" height="307" alt="image" src="https://github.com/user-attachments/assets/00a22128-2d5b-4b42-97e2-835915308125" />


## *Sprint 2 Review'da alınan kararlar:*

Her sprint sonunda tamamlanan görevler ve çalışan ürün ekran görüntüleri ile birlikte gözden geçirilir. Sprint Review notları acceptance criteria'ların karşılanıp karşılanmadığı kontrol edilerek tutulur.

## Tamamlanan Görevler

### Backend (Beyza)
Agentic AI mimarisi tamamlandı:

signal_agent.py — sepet, müşteri geçmişi ve yorum sinyallerini çıkarıyor
risk_agent.py — kural tabanlı (baseline) risk skoru hesaplıyor
action_agent.py — müşteri mesajı ve işletme aksiyonu üretiyor
orchestrator.py — Signal → Risk → Action akışını yönetiyor

POST /api/agent/analyze-cart çalışıyor ve test edildi
POST /api/predict çalışıyor ve test edildi
returnshield_agent_cart_scores.csv backend'e entegre edildi (cart_scores.py servisi)
GET /api/dashboard/summary eklendi — gerçek CSV'den high/medium/low risk dağılımı, önlenen iade tahmini, CO₂ hesabı
GET /api/agent/top-alerts eklendi — en yüksek riskli 4 sepeti gerçek veriden döndürüyor
/api/orders müşteri adlarını da döndürecek şekilde güncellendi


### Frontend (Taibenur)
Risk detail modal eklendi — satıra tıklayınca açılıyor
Agent flow görsel olarak gösteriliyor (SignalAgent → RiskAgent → ActionAgent)
Risk faktörleri, customer message ve recommended action panelde gösteriliyor
analyzeCart() fonksiyonu gerçek CSV verisine bağlandı
CO₂ kartı /api/dashboard/summary'den besleniyor (20.7kg, 9 returns prevented)
AI Alerts paneli /api/agent/top-alerts'ten dinamik dolduruluyor
cart.html müşteri sepet ekranı oluşturuldu:

Risk göstergesi (Medium Return Risk %76)
Yumuşak uyarı kartı
3 aksiyon butonu (beden rehberi, yorum özeti, alternatif beden)
Gerçek API bağlantısı

Müşteri adları sipariş tablosunda görünür hale getirildi
Sidebar sadeleştirildi (kullanılmayan linkler kaldırıldı)

### Data/ML (Osman)
6 notebook'luk pipeline tamamlandı:

01: Online Retail veri hazırlama

02: Baseline risk modeli (RF, LogReg, PR-AUC analizi)

03: Fit signal PoC (ModCloth + RentTheRunway)

04: Review signal PoC (beden, kalite, renk, olumsuz dil sinyalleri)

05: Mock cart features (tüm sinyaller sepet seviyesinde birleştirildi)

06: ReturnShield agent demo — risk_score, risk_level, top_reasons, suggested_action, dashboard_message üretildi


Ana çıktı dosyası hazırlandı: outputs/06_returnshield_agent_demo/returnshield_agent_cart_scores.csv
5 docs dosyası tamamlandı: data_dictionary.md, dataset_decision.md, model_summary.md, agent_output_schema.md, demo_cart_cases.md
Handoff raporu hazırlandı

## Acceptance Criteria Kontrolü
+ /api/predict ve /api/agent/analyze-cart endpoint'leri çalışıyor
  
+ ML modeli veya risk motoru API'den çağrılıyor, response şeması frontend ile uyumlu
  
+ Risk nedenleri ve AI mesajı ekranda gösteriliyor
  
+ Precision/Recall/F1 raporu, model dosyası ve açıklanabilirlik grafiği hazır (outputs/ klasöründe)
  
+ analyze-cart response içinde agents_used, reasons, customer_message, merchant_action dönüyor


## *Sprint Retrospective'de alınan kararlar*

Sprint Retrospective notları:

## Ne iyi gitti?

+ Agentic AI mimarisi (Orchestrator, Signal, Risk, Action) sorunsuz kuruldu
+ TÜ2'nin ML pipeline çıktısı (returnshield_agent_cart_scores.csv) backend'e başarıyla entegre edildi
+ Frontend ve backend uçtan uca bağlandı — gerçek CSV verisi dashboard'da görünür hale geldi
+ /api/dashboard/summary ve /api/agent/top-alerts ile stat kartları ve AI Alerts gerçek veriden besleniyor
+ cart.html müşteri sepet ekranı tamamlandı, 3 aksiyon butonu ve gerçek API bağlantısı çalışıyor
+ Risk detail panel açılıyor, agent flow görsel olarak gösteriliyor


## Ne zorladı?
pandas requirements.txt'te eksikti, Docker rebuild gerekti

CSV entegrasyonunda path problemi yaşandı (Docker volume mount gerekti)

Data/ML tarafında pkl export yapılmadı, bunun yerine hazır agent demo çıktısı kullanıldı

AI Alerts başlangıçta statik mock'tu, dinamik hale getirilmesi ek iş gerektirdi


## Neyi değiştirmeliyiz?
Sprint 3'te demo akışı baştan sona prova edilecek — video çekiminden önce tüm ekip aynı anda test edecek

README kurulum adımları Sprint 3'te netleştirilecek — tek komutla çalışır hale getirilecek

AI Alerts'teki cart_id isimleri daha okunabilir hale getirilecek


## Sonraki Sprint Aksiyonu
Demo videosu çekilecek (3 dakika, PDF'deki akış sırasıyla)

/api/memory/logs endpoint'i eklenebilir (opsiyonel, agent log gösterimi için)

Sunum slaytları hazırlanacak

README final düzenlemesi yapılacak

Sprint 3 scrum dokümantasyonu tamamlanacak


### Frontend gözlemi 
Modal ve agent flow görseli jüri için güçlü bir demo noktası oldu
cart.html müşteri tarafını başarıyla simüle ediyor


### Data/ML gözlemi 
6 notebook'luk pipeline tamamlandı, tüm çıktılar outputs/ altında toplandı

Handoff raporu ve 5 docs dosyası hazırlandı — veri şeffaflığı sağlandı

pkl export yapılmadı ama returnshield_agent_cart_scores.csv aynı işi görüyor, demo etkilenmedi


Sprint 3'te demo akışı baştan sona prova edilecek — video çekiminden önce tüm ekip aynı anda test edecek
README kurulum adımları Sprint 3'te netleştirilecek — tek komutla çalışır hale getirilecek
AI Alerts'teki cart_id isimleri daha okunabilir hale getirilecek

*Ürün Durumu: Ekran görüntüleri:

<img width="1600" height="763" alt="image" src="https://github.com/user-attachments/assets/f23f1820-d342-43a5-a8fe-879dac9d9a0d" />
<img width="489" height="724" alt="image" src="https://github.com/user-attachments/assets/d97f116e-46e2-4de4-a33d-f575e69feee2" />
<img width="386" height="371" alt="image" src="https://github.com/user-attachments/assets/6786b3c8-afe2-4e92-ad0d-6a00b5aa544a" />
<img width="1060" height="792" alt="image" src="https://github.com/user-attachments/assets/efd52186-1d79-4d9a-81b6-c44de2c856de" />


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



