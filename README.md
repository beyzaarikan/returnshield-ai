# ReturnShield AI

E-ticarette iade riskini önceden tespit eden AI destekli yönetim paneli.

## Takım

| Kişi | Rol |
|------|-----|
| Takım Üyesi | Backend + AI Lead |
| Takım Üyesi 1 | Frontend |
| Takım Üyesi 2 | Data / ML |

## Proje Yapısı

```
returnshield-ai/
├── docker-compose.yml
├── backend/          ← FastAPI + PostgreSQL
├── frontend/         ← Dashboard (HTML + Tailwind)
└── notebooks/        ← EDA + ML modelleri
```

---

## Repo'yu İlk Kez Kurma

### Gereksinimler

- [Git](https://git-scm.com/downloads)
- Kendi rolüne göre aşağıdaki araçlardan biri:

| Rol | Gereken |
|-----|---------|
| Backend | Docker Desktop |
| Frontend | Sadece tarayıcı yeterli |
| Data/ML | Python 3.10+ ve Jupyter |

### 1. Repo'yu clone'la

```bash
git clone https://github.com/[takım-adı]/returnshield-ai.git
cd returnshield-ai
```

### 2. Kendi branch'ini aç

```bash
git checkout -b [kendi-ismin]/[görev-adı]
# Örnek: git checkout -b ahmet/frontend-layout
```

---

## Backend'i Çalıştırma 

Docker Desktop açıkken proje kökünde:

```bash
docker compose up
```

Backend hazır olduğunda: `http://localhost:8000/docs`

---

## Frontend'i Çalıştırma

Docker'a gerek yok. `frontend/` klasörüne gir, `index.html`'i tarayıcıda aç.

Canlı önizleme için (opsiyonel):

```bash
# Python varsa:
python -m http.server 3000

# Node varsa:
npx serve .
```

Sonra `http://localhost:3000` aç.

API bağlantısı için backend'in çalışıyor olması lazım (`http://localhost:8000`). Backend çalışmıyorsa `js/api.js` otomatik olarak mock data'ya geçer, çalışmaya devam edersin.

---

## Data / ML Çalıştırma

Docker'a gerek yok. `notebooks/` klasöründe çalışırsın.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook
```

---

## Branch & Pull Request Kuralları

- Kimse direkt `main`'e push yapmaz
- Herkes kendi branch'inde çalışır: `[isim]/[görev]`
- Bitince GitHub'da Pull Request aç → base: `main`
- Takım Üyesi merge eder

---

## Scrum Board

GitHub Projects Board linki 
https://github.com/users/beyzaarikan/projects/2/views/1?layout=board

Kolonlar: `Backlog → Sprint 1 → In Progress  → Done`

---

## API Endpoints (Sprint 1)

Base URL: `http://localhost:8000`

| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | `/api/orders` | Tüm siparişler |
| GET | `/api/orders/{id}` | Tek sipariş |
| GET | `/api/users` | Tüm kullanıcılar |

Detaylı döküman: `backend/API_CONTRACT.md`