const BASE_URL = 'http://localhost:8000';

const MOCK_ORDERS = [
  { id: 1, customer: 'Ayşe K.', product: 'Oversize Sweatshirt M+L', order_hour: '23:14', risk_score: 0.85, risk_label: 'high', is_returned: true },
  { id: 2, customer: 'Zeynep A.', product: 'Elbise S+M', order_hour: '01:32', risk_score: 0.78, risk_label: 'high', is_returned: true },
  { id: 3, customer: 'Fatma B.', product: 'Slim Fit Pantolon', order_hour: '19:45', risk_score: 0.52, risk_label: 'mid', is_returned: false },
  { id: 4, customer: 'Mehmet D.', product: 'Spor Ayakkabı', order_hour: '14:20', risk_score: 0.18, risk_label: 'low', is_returned: false },
  { id: 5, customer: 'Ali S.', product: 'Kışlık Mont', order_hour: '11:05', risk_score: 0.12, risk_label: 'low', is_returned: false },
];

const MOCK_ALERTS = [
  { level: 'high', name: 'Ayşe K. — gece + 2 beden', desc: 'Aynı ürünün M ve L bedeni sepette. Gece 23:14.' },
  { level: 'high', name: 'Zeynep A. — tekrar iade', desc: 'Son 30 günde 4. iade. Gece 01:32 siparişi.' },
  { level: 'mid', name: 'Fatma B. — yorum uyarısı', desc: '"Kalıbı dar" şikayeti olan üründen sipariş.' },
  { level: 'mid', name: 'Can T. — fiyat anomalisi', desc: 'Yüksek fiyatlı üründe ilk kez sipariş.' },
];

async function getOrders() {
  try {
    const res = await fetch(`${BASE_URL}/api/orders`);
    if (!res.ok) throw new Error('API hazır değil');
    return await res.json();
  } catch {
    console.warn('API bağlanamadı, mock data kullanılıyor.');
    return MOCK_ORDERS;
  }
}

function riskBadge(label) {
  const map = {
    high: ['badge-high', 'Yüksek Risk'],
    mid:  ['badge-mid',  'Orta Risk'],
    low:  ['badge-low',  'Düşük Risk'],
  };
  const [cls, text] = map[label] || map['low'];
  return `<span class="badge ${cls}">${text}</span>`;
}

function riskBar(score, label) {
  const fillClass = label === 'high' ? 'fill-high' : label === 'mid' ? 'fill-mid' : 'fill-low';
  const pct = Math.round(score * 100);
  return `<div class="score-wrap">
    <div class="score-bar"><div class="score-fill ${fillClass}" style="width:${pct}%"></div></div>
    %${pct}
  </div>`;
}

async function renderOrdersTable() {
  const orders = await getOrders();
  const tbody = document.getElementById('orders-table-body');
  if (!tbody) return;

  orders.sort((a, b) => b.risk_score - a.risk_score);

  tbody.innerHTML = orders.map(o => `
    <tr>
      <td>${o.customer || o.name || '—'}</td>
      <td>${o.product || o.product_name || '—'}</td>
      <td>${o.order_hour || '—'}</td>
      <td>${riskBar(o.risk_score, o.risk_label)}</td>
      <td>${riskBadge(o.risk_label)}</td>
    </tr>
  `).join('');

  const total = orders.length;
  const highRisk = orders.filter(o => o.risk_label === 'high').length;
  const returned = orders.filter(o => o.is_returned).length;

  document.getElementById('stat-high').textContent = highRisk;
  document.getElementById('stat-total').textContent = total;
  document.getElementById('stat-return').textContent = '%' + Math.round((returned / total) * 100);
}

function renderAlerts() {
  const list = document.getElementById('alerts-list');
  if (!list) return;
  list.innerHTML = MOCK_ALERTS.map(a => `
    <div class="alert-item">
      <div class="alert-dot dot-${a.level}"></div>
      <div>
        <div class="alert-name">${a.name}</div>
        <div class="alert-desc">${a.desc}</div>
      </div>
    </div>
  `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
  renderOrdersTable();
  renderAlerts();
});
