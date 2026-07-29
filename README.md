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
Offline model-derived risk ranking (Random Forest/Logistic Regression) ve açıklanabilir rules baseline
İsteğe bağlı Gemini destekli müşteri mesajı; API key veya quota yoksa template fallback
Agentic AI mimarisi: Orchestrator, Signal, Risk, Action agent'ları
Müşteri ekranında yumuşak, manipülatif olmayan uyarı mesajı
İşletme dashboard'unda riskli sipariş listesi ve aksiyon önerileri
Sürdürülebilirlik farkındalığı (önlenen iade ile CO₂/kargo tasarrufu)

## Hedef Kitle
Moda/tekstil/ayakkabı kategorisinde satış yapan e-ticaret işletmeleri ve bu platformlardan alışveriş yapan online müşteriler. İşletme tarafında kategori yöneticileri ve müşteri destek ekipleri; müşteri tarafında satın alma kararı verirken emin olamayan kullanıcılar.

# Sprint 1

*Backlog Düzeni ve Story Seçimleri*
Bu proje local ortamda çalışmaktadır. Scrum board olarak GitHub Projects kullanılmıştır ancak GitHub Projects linkleri harici kullanıcılara açık olmadığından link paylaşımı mümkün olmamaktadır.
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

GitHub Projects board'unda kartlar Backlog → Sprint 2 → to-do → In Progress  → Done kolonlarında takip edilmektedir. Her kart bir görevi temsil eder ve ilgili kişiye atanmıştır.

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
  
+ Runtime API'de rules baseline risk motoru çağrılıyor; demo cart'larda precomputed agent output kullanılıyor ve response şeması frontend ile uyumlu
  
+ Risk nedenleri ve AI mesajı ekranda gösteriliyor
  
+ Precision/Recall/F1 raporları ve açıklanabilirlik grafikleri outputs/ klasöründe hazır; runtime model artifact'ı projeye dahil değildir
  
+ analyze-cart response içinde agents_used, reasons, customer_message, merchant_action, message_source ve llm_used dönüyor


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

Data/ML tarafında pkl/joblib export yapılmadı; notebook model skorları offline pipeline üzerinden agent demo CSV çıktısına aktarıldı

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

pkl/joblib export yapılmadı. returnshield_agent_cart_scores.csv yalnızca offline demo çıktısıdır; runtime model artifact'ı yerine geçmez. Demo akışı precomputed skorlarla çalışır.


Sprint 3'te demo akışı baştan sona prova edilecek — video çekiminden önce tüm ekip aynı anda test edecek
README kurulum adımları Sprint 3'te netleştirilecek — tek komutla çalışır hale getirilecek
AI Alerts'teki cart_id isimleri daha okunabilir hale getirilecek

*Ürün Durumu: Ekran görüntüleri:

<img width="1600" height="763" alt="image" src="https://github.com/user-attachments/assets/f23f1820-d342-43a5-a8fe-879dac9d9a0d" />
<img width="489" height="724" alt="image" src="https://github.com/user-attachments/assets/d97f116e-46e2-4de4-a33d-f575e69feee2" />
<img width="386" height="371" alt="image" src="https://github.com/user-attachments/assets/6786b3c8-afe2-4e92-ad0d-6a00b5aa544a" />
<img width="1060" height="792" alt="image" src="https://github.com/user-attachments/assets/efd52186-1d79-4d9a-81b6-c44de2c856de" />


# Sprint 3

GitHub Projects board'unda kartlar Sprint 3 → to-do → In Progress  → Done kolonlarında takip edilmektedir. Her kart bir görevi temsil eder ve ilgili kişiye atanmıştır.

Backlog Düzeni ve Story Seçimleri
Backlog, öncelikli görevlere göre düzenlenmiş ve her sprint için tahmin edilen puan sınırını aşmayacak şekilde seçimler yapılmıştır. Görevler backend, frontend ve data/ML olmak üzere üç sorumluluk alanına bölünmüş; her alan kendi içinde bağımsız çalışabilecek şekilde tasarlanmıştır. Her sprint başında takım olarak görev tahmini yapılmış, story'ler task'lere bölünmüş ve GitHub Projects board'unda ilgili kişiye atanmıştır. Sprint içinde tamamlanan görevler "Done" kolonuna taşınmış, tamamlanamayan görevler bir sonraki sprint backlog'una aktarılmıştır.

Sprint 1 seçimleri: Temel altyapı — repo kurulumu, FastAPI + Docker, veritabanı, dashboard layout, EDA notebook.

Sprint 2 seçimleri: Core AI — agent mimarisi, CSV entegrasyonu, risk paneli, müşteri sepet ekranı, ML pipeline tamamlama.

Sprint 3 seçimleri: Cila ve teslim — Gemini entegrasyonu, memory log, test suite, ek demo senaryoları, README, video.

 ### Sprint Board Update Screenshots
<img width="1911" height="814" alt="image" src="https://github.com/user-attachments/assets/bd52fae0-8926-453f-9e87-f03e270f7bc2" />
<img width="1878" height="849" alt="image" src="https://github.com/user-attachments/assets/2b12f9e7-228f-47d6-895c-83906403d2b5" />
<img width="1915" height="815" alt="image" src="https://github.com/user-attachments/assets/0471b5a9-c88a-4528-8947-fd22adb601e3" />

## *Daily Scrum*
Daily Scrum toplantıları zamansal sebeplerden ötürü WhatsApp üzerinden yazılı olarak da yapılmaktadır.

BEYZA (Backend / Scrum Master)
Gün 1
Sprint 2 tamamlandı, tüm dökümanlar GitHub'a yüklendi.
Gemini API entegrasyonu — action_agent.py güncellendi, google-generativeai paketi eklendi, Docker rebuild yapıldı

Gün 2
Gemini entegrasyonu çalışıyor, customer_message dinamik üretiliyor.
Agent memory log sistemi eklendi (/api/agent/logs endpoint'i), her analyze-cart çağrısı loglanıyor

Gün 3
Memory log sistemi tamamlandı, Swagger'da test edildi.
top-alerts endpoint'ine müşteri ismi mapping'i eklendi, AI Alerts paneli okunabilir hale getirildi.

Gün 4
README tamamlandı, tüm dosyalar son kontrol yapıldı.
Demo provası yapıldı, Sprint 3 dökümanları hazırlandı, video çekimi.

OSMAN (Data / ML)
Gün 1
Sprint 2 notebook'ları ve dökümanlar GitHub'a yüklendi.
final_model_summary.md tamamlandı — veri kaynakları, model sınırlılıkları, prototip notu.

Gün 2
Model özeti tamamlandı.
Demo sepet senaryoları için ek analiz yapıldı, demo_cart_cases.md güncellendi.

Gün 3
Demo senaryoları netleştirildi.
Sunum slaytları için model metrikleri ve SHAP/feature importance grafikleri hazırlandı.

Gün 4
Sunum materyalleri hazırlandı.
Demo provası yapıldı, veri sınırlılıkları soruları için hazırlık yapıldı.

TAİBENUR (Frontend)
Gün 1
Sprint 2 frontend değişiklikleri tamamlandı.
cart3.html oluşturuldu — impulse buying senaryosu, 4 ürünlü sepet, length issue sinyali

Gün 2
cart3.html tamamlandı ve test edildi.
cart4.html oluşturuldu — repeat returner senaryosu, fit sinyali yüksek müşteri.

Gün 3
cart4.html tamamlandı.
Sidebar'a cart3 ve cart4 linkleri eklendi, tüm 4 demo senaryosu test edildi.

Gün 4
Tüm demo sayfaları test edildi.
Status kolonu kaldırıldı, Risk Analysis kolonuna "Click to analyze" eklendi, son UI düzenlemeleri yapıldı.

## *Sprint 3 Review'da alınan kararlar:*

Her sprint sonunda tamamlanan görevler ve çalışan ürün ekran görüntüleri ile birlikte gözden geçirilir. Sprint Review notları acceptance criteria'ların karşılanıp karşılanmadığı kontrol edilerek tutulur.

Backend (Beyza):

Gemini API entegrasyonu — action_agent.py LLM destekli mesaj üretiyor; quota/key yoksa template fallback devreye giriyor, message_source ve llm_used alanları response'ta dönüyor
GET /api/agent/logs — memory log sistemi, her analyze-cart çağrısı loglanıyor
top-alerts endpoint'i — cart_id yerine müşteri isimleri gösteriliyor
CORS FRONTEND_ORIGINS ile sınırlandırıldı
backend/.env opsiyonel hale getirildi

Backend (Osman):

Docker başlangıç akışı iyileştirildi — PostgreSQL healthcheck, otomatik migration ve seed.
/health ve /ready endpoint'leri eklendi
API response sözleşmeleri standardize edildi — risk seviyeleri low/medium/high, analysis_mode, data_source, scoring_mode alanları eklendi
15 otomatik test yazıldı ve geçti (pytest tests/)
Pydantic v2, SQLAlchemy 2 deprecated kullanımlar düzeltildi
README final düzeni — kurulum, scoring açıklaması, demo CSV vs canlı baseline ayrımı

Frontend (Taibenur):

cart3.html — impulse buying senaryosu, 4 ürün, length issue (%93 High Risk)
cart4.html — repeat returner senaryosu, fit sinyali (%95 High Risk)
Status kolonu kaldırıldı, "Click to analyze" eklendi
Sidebar sadeleştirildi

## Acceptance Criteria:

 + docker compose up --build -d ile sistem ayağa kalkıyor.
 + /health ve /ready endpoint'leri başarılı dönüyor.
 + 15 test geçti.
 + Demo videosu çekildi.
 + 4 demo senaryosu çalışıyor.
 + Gemini çalışınca LLM mesajı, quota dolunca template fallback devreye giriyor.

## *Sprint Retrospective'de alınan kararlar*

Sprint Retrospective notları:

## Ne iyi gitti?
Gemini entegrasyonu sorunsuz tamamlandı, customer_message artık dinamik ve doğal.
Memory log sistemi hızla kuruldu, "agentic hafıza" iddiası kanıtlanabilir hale geldi.
4 farklı demo senaryosu birbirini tamamlıyor — jüriye geniş bir bakış açısı sunuluyor.
Tüm ekip demo provasına katıldı, akış netleşti.

## Ne zorladı?
+GitHub Projects linki harici kullanıcılara açık olmadığı için board paylaşımı sorun yarattı
+Local ortamda çalışıyor, canlı deploy yapılamadı
+Gemini API bazen yavaş yanıt veriyor, demo sırasında bekleme süresi oluşabiliyor
+Neyi değiştirmeliyiz?
+Gelecekte deploy adımı (Railway/Render) sprint 2'ye alınmalı, sprint 3'te hazır olmalı
+Scrum board için baştan Miro veya Notion kullanılmalı, link paylaşımı sorunsuz olur
+Gemini yanıt süresi için timeout ve fallback mekanizması iyileştirilmeli

## Genel Değerlendirme
+ReturnShield AI, 3 sprint boyunca sıfırdan tam çalışan bir agentic AI sistemine dönüştü.
+Backend agent mimarisi, gerçek ML pipeline çıktısı ve interaktif demo sayfaları ile projenin tüm teknik kriterleri karşılandı. 
+Gemini LLM entegrasyonu ve memory log sistemi ile "agentic" yapı somut kanıtlarla gösterilebildi.

*Ürün Durumu: Ekran görüntüleri:
<img width="1600" height="774" alt="WhatsApp Image 2026-07-23 at 15 15 58" src="https://github.com/user-attachments/assets/c0e63af6-2ae4-457b-a460-b983747a8ae3" />
<img width="668" height="907" alt="WhatsApp Image 2026-07-23 at 15 15 58 (1)" src="https://github.com/user-attachments/assets/0c74089e-a917-421a-bcae-0996ed7ec2ce" />


### Gereksinimler

## Backend'i Çalıştırma 

Docker Desktop açıkken proje kökünde:

```bash
docker compose up --build -d
```

Backend Swagger dokümantasyonu:

`http://localhost:8000/docs`

Gemini mesaj üretimini etkinleştirmek istersen `backend/.env` dosyasına geçerli bir `GEMINI_API_KEY` ekleyebilirsin. Key veya quota yoksa sistem template mesajıyla çalışmaya devam eder.

---

## Frontend'i Çalıştırma
Frontend Docker Compose içindeki Nginx servisi üzerinden çalışır:

`http://localhost:3000`

---

## Data / ML Çalıştırma

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook
```



