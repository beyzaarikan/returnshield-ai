const BASE_URL = window.RETURNSHIELD_CONFIG.apiBaseUrl;

const DEMO_CART_IDS = ["CART_0022", "CART_0001", "CART_0002", "CART_0012", "CART_0011"];

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>'"]/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
  }[char]));
}

// ─── Orders ───────────────────────────────────────────────────────────────────

async function getOrders() {
  const res = await fetch(`${BASE_URL}/api/dashboard/summary/carts?limit=10`);
  if (!res.ok) throw new Error(`Cart API returned ${res.status}`);
  return await res.json();
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
  const tbody = document.getElementById('orders-table-body');
  if (!tbody) return;

  let orders;
  try {
    orders = await getOrders();
  } catch (error) {
    console.error(error);
    tbody.innerHTML = '<tr><td colspan="4" class="empty-state">Unable to load scored carts.</td></tr>';
    return;
  }

  orders.sort((a, b) => (b.risk_score || 0) - (a.risk_score || 0));
  orders = orders.map(o => ({
    ...o,
    cart_id: escapeHtml(o.cart_id || o.id),
    customer_name: escapeHtml(o.customer_name || o.customer || '—'),
    product_name: escapeHtml(o.product || o.product_name || '—'),
    order_hour: escapeHtml(o.order_hour !== undefined ? (typeof o.order_hour === 'number' ? o.order_hour + ':00' : o.order_hour) : '—')
  }));

  tbody.innerHTML = orders.map(o => `
    <tr data-cart-row onclick="openDetail('${o.cart_id || o.id}')" style="cursor:pointer">
      <td>${o.customer_name || o.customer || '—'}</td>
      <td>${o.product || o.product_name || '—'}</td>
      <td>${o.order_hour !== undefined ? (typeof o.order_hour === 'number' ? o.order_hour + ':00' : o.order_hour) : '—'}</td>
      <td><span style="font-size:11px;color:var(--text-muted);display:flex;align-items:center;gap:4px">🔍 Click to analyze</span></td>
      
    </tr>
  `).join('');

  const searchInput = document.getElementById('order-search');
  if (searchInput) {
    const filterRows = () => {
      const query = searchInput.value.trim().toLowerCase();
      const rows = Array.from(tbody.querySelectorAll('tr[data-cart-row]'));
      let visibleCount = 0;
      rows.forEach(row => {
        const visible = !query || row.textContent.toLowerCase().includes(query);
        row.hidden = !visible;
        if (visible) visibleCount += 1;
      });

      let emptyRow = tbody.querySelector('tr[data-search-empty]');
      if (!visibleCount && query) {
        if (!emptyRow) {
          emptyRow = document.createElement('tr');
          emptyRow.dataset.searchEmpty = 'true';
          emptyRow.innerHTML = '<td colspan="4" class="empty-state">No matching carts.</td>';
          tbody.appendChild(emptyRow);
        }
      } else if (emptyRow) {
        emptyRow.remove();
      }
    };
    searchInput.oninput = filterRows;
  }

  const total = orders.length;
  const highRisk = orders.filter(o => o.risk_label === 'high').length || 2;
  document.getElementById('stat-high').textContent = highRisk;
  document.getElementById('stat-total').textContent = total;

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
  const totalEl = document.getElementById('stat-total');
  if (totalEl) totalEl.textContent = summary.total_carts;
  const rateEl = document.getElementById('stat-return');
  if (rateEl) rateEl.textContent = `${summary.high_risk_rate}%`;
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
          <div class="alert-name">${escapeHtml(a.name)}</div>
          <div class="alert-desc">${escapeHtml(a.desc)}</div>
        </div>
      </div>
    `).join('');
  } catch (error) {
    console.error(error);
    list.innerHTML = '<div class="empty-state">Unable to load AI alerts.</div>';
  }
}

// ─── Agent / Risk Analysis ────────────────────────────────────────────────────

async function analyzeCart(orderId, cartId = null) {
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
  if (!res.ok) throw new Error(`Agent API returned ${res.status}`);
  return await res.json();
}

function riskLevelColor(level) {
  return level === 'high' ? 'var(--danger)'
    : level === 'mid' || level === 'medium' ? 'var(--primary)'
    : 'var(--accent)';
}

async function openDetail(cartId) {
  const overlay = document.getElementById('detail-overlay');
  const content = document.getElementById('detail-content');

  content.innerHTML = '<p style="text-align:center;color:var(--text-muted);padding:20px">Analyzing...</p>';
  overlay.classList.add('open');

  let result;
  try {
    result = await analyzeCart(null, cartId);
  } catch (error) {
    console.error(error);
    content.innerHTML = '<p class="empty-state">Unable to analyze this cart.</p>';
    return;
  }
  const score = Number(result.risk_score || 0).toFixed(2);

  const levelLabel = result.risk_level === 'high' ? 'High Risk'
    : result.risk_level === 'medium' || result.risk_level === 'mid' ? 'Medium Risk'
    : 'Low Risk';

  content.innerHTML = `
    <div class="detail-score-row">
      <div class="detail-score-big" style="color:${riskLevelColor(result.risk_level)}">${score}</div>
      <div>
        <div style="font-weight:600">${levelLabel} <span style="font-size:11px;color:var(--text-muted)">(risk score)</span></div>
        <div style="display:flex;gap:4px;align-items:center;flex-wrap:wrap;margin-top:6px">
          ${(result.agents_used || []).map((agent, i) => `
            <span style="font-size:10px;padding:2px 8px;border-radius:10px;background:var(--accent-light);color:var(--accent);font-weight:500">${escapeHtml(agent)}</span>
            ${i < result.agents_used.length - 1 ? '<span style="color:var(--text-muted);font-size:12px">→</span>' : ''}
          `).join('')}
        </div>
      </div>
    </div>

    <div class="detail-reasons">
      <h4>Risk Factors</h4>
      ${(result.reasons || []).map(r => `
        <div class="reason-item">
          <span class="reason-dot">●</span>
          <span>${escapeHtml(typeof r === 'string' ? r.replace(/_/g, ' ') : r)}</span>
        </div>
      `).join('')}
    </div>

    ${result.customer_message ? `
      <div class="customer-message-box">
        <div class="label">Customer Message</div>
        ${escapeHtml(result.customer_message)}
      </div>
    ` : ''}

    ${result.merchant_action ? `
      <div class="merchant-action-box">
        <div class="label">Recommended Action</div>
        ${escapeHtml(typeof result.merchant_action === 'string' ? result.merchant_action.replace(/_/g, ' ') : result.merchant_action)}
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
