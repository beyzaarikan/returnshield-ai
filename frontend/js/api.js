const BASE_URL = 'http://localhost:8000';

const MOCK_ORDERS = [
  { id: 1, customer: 'Alice J.', product: 'Oversized Sweatshirt M+L', order_hour: '23:14', risk_score: 0.85, risk_label: 'high', is_returned: true },
  { id: 2, customer: 'Sarah W.', product: 'Dress S+M', order_hour: '01:32', risk_score: 0.78, risk_label: 'high', is_returned: true },
  { id: 3, customer: 'Emma B.', product: 'Slim Fit Trousers', order_hour: '19:45', risk_score: 0.52, risk_label: 'mid', is_returned: false },
  { id: 4, customer: 'Michael D.', product: 'Sport Shoes', order_hour: '14:20', risk_score: 0.18, risk_label: 'low', is_returned: false },
  { id: 5, customer: 'James S.', product: 'Winter Jacket', order_hour: '11:05', risk_score: 0.12, risk_label: 'low', is_returned: false },
];

const MOCK_ALERTS = [
  { level: 'high', name: 'Alice J. — night + 2 sizes', desc: 'Same product added in size M and L. Order placed at 23:14.' },
  { level: 'high', name: 'Sarah W. — repeat return', desc: '4 returns in the last 30 days. Order placed at 01:32.' },
  { level: 'mid', name: 'Emma B. — review warning', desc: 'Order for a product with "runs small" reviews.' },
  { level: 'mid', name: 'Can T. — price anomaly', desc: 'First-time order for a high-priced item.' },
];

const DEMO_CART_IDS = ["CART_0022", "CART_0001", "CART_0002", "CART_0012", "CART_0011"];

// ─── Orders ───────────────────────────────────────────────────────────────────

async function getOrders() {
  try {
    const res = await fetch(`${BASE_URL}/api/orders`);
    if (!res.ok) throw new Error('API not ready');
    return await res.json();
  } catch {
    console.warn('API connection failed, using mock data.');
    return MOCK_ORDERS;
  }
}

function riskBadge(label) {
  const map = {
    high:   ['badge-high', 'High Risk'],
    medium: ['badge-mid',  'Medium Risk'],
    mid:    ['badge-mid',  'Medium Risk'],
    low:    ['badge-low',  'Low Risk'],
  };
  const [cls, text] = map[label] || map['low'];
  return `<span class="badge ${cls}">${text}</span>`;
}

function riskBar(score, label) {
  if (score === undefined || score === null || isNaN(score)) {
    return '<span style="color:var(--text-muted);font-size:11px">—</span>';
  }
  const fillClass = label === 'high' ? 'fill-high' : label === 'mid' || label === 'medium' ? 'fill-mid' : 'fill-low';
  const pct = Math.round(score * 100);
  return `<div class="score-wrap">
    <div class="score-bar"><div class="score-fill ${fillClass}" style="width:${pct}%"></div></div>
    ${pct}%
  </div>`;
}

async function renderOrdersTable() {
  const orders = await getOrders();
  const tbody = document.getElementById('orders-table-body');
  if (!tbody) return;

  orders.sort((a, b) => (b.risk_score || 0) - (a.risk_score || 0));

  tbody.innerHTML = orders.map(o => `
    <tr onclick="openDetail(${o.id})" style="cursor:pointer">
      <td>${o.customer_name || o.customer || '—'}</td>
      <td>${o.product || o.product_name || '—'}</td>
      <td>${o.order_hour !== undefined ? o.order_hour + ':00' : '—'}</td>
      <td><span style="font-size:11px;color:var(--text-muted);display:flex;align-items:center;gap:4px">🔍 Click to analyze</span></td>
      
    </tr>
  `).join('');

  const total = orders.length;
  const highRisk = orders.filter(o => o.risk_label === 'high').length || 2;
  const returned = orders.filter(o => o.is_returned).length;

  document.getElementById('stat-high').textContent = highRisk;
  document.getElementById('stat-total').textContent = total;
  document.getElementById('stat-return').textContent = Math.round((returned / total) * 100) + '%';

  // Sustainability estimate
  try {
  const summaryRes = await fetch(`${BASE_URL}/api/dashboard/summary`);
  const summary = await summaryRes.json();
  const co2El = document.getElementById('co2-value');
  const returnsEl = document.getElementById('returns-prevented-text');
  const highEl = document.getElementById('stat-high');
  if (co2El) co2El.textContent = `${summary.co2_saved_kg}kg`;
  if (returnsEl) returnsEl.textContent = `${summary.returns_prevented_est} returns prevented (est.)`;
  if (highEl) highEl.textContent = summary.high_risk;
} catch(e) {
  console.warn('Summary API failed');
}
}

async function renderAlerts() {
  const list = document.getElementById('alerts-list');
  if (!list) return;

  try {
    // En yüksek riskli 4 sepeti CSV'den çek
    const res = await fetch(`${BASE_URL}/api/agent/top-alerts`);
    if (!res.ok) throw new Error();
    const alerts = await res.json();
    list.innerHTML = alerts.map(a => `
      <div class="alert-item">
        <div class="alert-dot dot-${a.level === 'medium' ? 'mid' : a.level}"></div>
        <div>
          <div class="alert-name">${a.name}</div>
          <div class="alert-desc">${a.desc}</div>
        </div>
      </div>
    `).join('');
  } catch {
    // Fallback: mock alerts
    list.innerHTML = MOCK_ALERTS.map(a => `
      <div class="alert-item">
        <div class="alert-dot dot-${a.level === 'medium' ? 'mid' : a.level}"></div>
        <div>
          <div class="alert-name">${a.name}</div>
          <div class="alert-desc">${a.desc}</div>
        </div>
      </div>
    `).join('');
  }
}

// ─── Agent / Risk Analysis ────────────────────────────────────────────────────

async function analyzeCart(orderId, cartId = null) {
  try {
    const body = {
      user_id: 1,
      cart_items: [
        { product_id: "DEMO", size: "M", price: 349, hour: 23, review_summary: "runs small" }
      ]
    };
    if (cartId) body.cart_id = cartId;

    const res = await fetch(`${BASE_URL}/api/agent/analyze-cart`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!res.ok) throw new Error('Agent API not ready');
    return await res.json();
  } catch {
    console.warn('Agent API connection failed, using mock result.');
    return {
      risk_score: 0.84,
      risk_level: "high",
      agents_used: ["SignalAgent", "RiskAgent", "ActionAgent"],
      reasons: ["high_transaction_model_rank", "large_cart_size", "length_issue_signal"],
      customer_message: "Fit-related signals are elevated. Show size and fit guidance.",
      merchant_action: "show_size_guidance_before_checkout"
    };
  }
}

function riskLevelColor(level) {
  return level === 'high' ? 'var(--danger)'
    : level === 'mid' || level === 'medium' ? 'var(--primary)'
    : 'var(--accent)';
}

async function openDetail(orderId) {
  const overlay = document.getElementById('detail-overlay');
  const content = document.getElementById('detail-content');

  content.innerHTML = '<p style="text-align:center;color:var(--text-muted);padding:20px">Analyzing...</p>';
  overlay.classList.add('open');

  const cartId = DEMO_CART_IDS[(orderId - 1) % DEMO_CART_IDS.length];
  const result = await analyzeCart(orderId, cartId);
  const pct = Math.round(result.risk_score * 100);

  const levelLabel = result.risk_level === 'high' ? 'High Risk'
    : result.risk_level === 'medium' || result.risk_level === 'mid' ? 'Medium Risk'
    : 'Low Risk';

  content.innerHTML = `
    <div class="detail-score-row">
      <div class="detail-score-big" style="color:${riskLevelColor(result.risk_level)}">${pct}%</div>
      <div>
        <div style="font-weight:600">${levelLabel}</div>
        <div style="display:flex;gap:4px;align-items:center;flex-wrap:wrap;margin-top:6px">
          ${result.agents_used.map((agent, i) => `
            <span style="font-size:10px;padding:2px 8px;border-radius:10px;background:var(--accent-light);color:var(--accent);font-weight:500">${agent}</span>
            ${i < result.agents_used.length - 1 ? '<span style="color:var(--text-muted);font-size:12px">→</span>' : ''}
          `).join('')}
        </div>
      </div>
    </div>

    <div class="detail-reasons">
      <h4>Risk Factors</h4>
      ${result.reasons.map(r => `
        <div class="reason-item">
          <span class="reason-dot">●</span>
          <span>${typeof r === 'string' ? r.replace(/_/g, ' ') : r}</span>
        </div>
      `).join('')}
    </div>

    ${result.customer_message ? `
      <div class="customer-message-box">
        <div class="label">Customer Message</div>
        ${result.customer_message}
      </div>
    ` : ''}

    ${result.merchant_action ? `
      <div class="merchant-action-box">
        <div class="label">Recommended Action</div>
        ${typeof result.merchant_action === 'string' ? result.merchant_action.replace(/_/g, ' ') : result.merchant_action}
      </div>
    ` : ''}
  `;
}

function closeDetail() {
  document.getElementById('detail-overlay').classList.remove('open');
}

// ─── Init ─────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  renderOrdersTable();
  renderAlerts();
});
