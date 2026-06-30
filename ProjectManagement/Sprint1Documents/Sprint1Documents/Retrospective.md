# Sprint 1 Retrospective — ReturnShield AI

## Ne iyi gitti?
- Docker Compose kurulumu sorunsuz tamamlandı
- FastAPI + PostgreSQL entegrasyonu hızlı kuruldu
- Seed data demo senaryosuna uygun hazırlandı

## Ne zorladı?
- İç içe geçmiş backend klasör yapısı düzeltildi
- Alembic env.py'de DATABASE_URL environment variable'dan okunacak şekilde güncellendi

## Neyi değiştirmeliyiz?
- Sprint 2'de agent klasörleri baştan planlanacak
- TÜ1 ve TÜ2 ile daha erken sync yapılacak

## Sonraki Sprint Aksiyonu
- /api/agent/analyze-cart endpoint Sprint 2'nin ilk görevi
- TÜ2'nin pkl dosyası teslim tarihi Sprint 2 ortasına alındı

### Frontend gözlemi
-CSS değişken sistemi sayesinde tasarım hızlı kuruldu, renk değişikliği gerekirse tek yerden yapılabilir.
**Sprint 2 için:** Risk breakdown paneli ve müşteri sepet ekranı eklenecek, Georgina'nın /api/agent/analyze-cart endpoint'ini bekleyecek.

### Data/ML gözlemi
-UCI Online Retail dataset'i hızlıca bulundu ve feature engineering planlandığı gibi ilerledi. Return rate ve zaman bazlı feature'lar anlamlı sinyaller verdi.

-Veri dengesizliği (class imbalance) nedeniyle model performansı (PR-AUC) beklenenden düşük çıktı. Ayrıca çalışma notebook'larda ilerlerken GitHub'a düzenli push yapılmadı, bu da Sprint 1/Sprint 2 sınırının belirsizleşmesine yol açtı.

**Neyi değiştirmeliyiz:** Her gün sonunda küçük commit'ler atılacak, büyük iş bloklarının sonuna kadar beklenmeyecek.

