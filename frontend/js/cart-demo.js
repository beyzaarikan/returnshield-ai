const BASE_URL = 'http://localhost:8000';

const CART_DEMOS = {
  CART_0001: {
    user_id: 1,
    cart_items: [
      { product_id: 'DEMO-DRESS', size: 'M', price: 49.90, hour: 23, review_summary: 'runs small' },
      { product_id: 'DEMO-DRESS', size: 'L', price: 49.90, hour: 23, review_summary: '' }
    ]
  },
  CART_0022: {
    user_id: 2,
    cart_items: [
      { product_id: 'DEMO-FLORAL-DRESS', size: 'M', price: 89.90, hour: 23, review_summary: 'runs short, color looks different' }
    ]
  },
  CART_0007: { user_id: 3, cart_items: [] },
  CART_0036: { user_id: 4, cart_items: [] }
};

function toggleBox(id) {
  document.getElementById(id)?.classList.toggle('show');
}

function toggleSizeGuide() { toggleBox('cart-warning'); }
function toggleReviewSummary() { toggleBox('review-summary-box'); }
function suggestAlternativeSize() { toggleBox('alt-size-box'); }

async function loadCartAnalysis(cartId) {
  const demo = CART_DEMOS[cartId];
  if (!demo) throw new Error(`Unknown demo cart: ${cartId}`);

  const response = await fetch(`${BASE_URL}/api/agent/analyze-cart`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ ...demo, cart_id: cartId })
  });
  if (!response.ok) throw new Error(`Agent API returned ${response.status}`);
  return response.json();
}

function showAnalysisError(error) {
  console.error(error);
  const indicator = document.getElementById('risk-indicator');
  const warning = document.getElementById('cart-warning');
  if (indicator) indicator.classList.remove('show');
  if (warning) {
    const message = document.getElementById('cart-warning-text');
    if (message) message.textContent = 'Risk analysis is temporarily unavailable. Please try again.';
    warning.classList.add('show');
  }
}

window.addEventListener('DOMContentLoaded', async () => {
  const cartId = document.body.dataset.cartId;
  const signalTags = document.getElementById('signal-tags');
  if (signalTags) signalTags.style.display = 'flex';

  try {
    const result = await loadCartAnalysis(cartId);
    const level = result.risk_level || 'low';
    const dotClass = level === 'high' ? 'high' : level === 'medium' || level === 'mid' ? 'medium' : 'low';
    const label = level === 'high' ? 'High Return Risk'
      : level === 'medium' || level === 'mid' ? 'Medium Return Risk'
      : 'Low Return Risk';

    document.getElementById('risk-dot').className = `risk-dot ${dotClass}`;
    document.getElementById('risk-label-text').textContent = label;
    document.getElementById('risk-score-num').textContent = `${Math.round((result.risk_score || 0) * 100)}%`;
    document.getElementById('risk-indicator').classList.add('show');

    if (result.customer_message) {
      document.getElementById('cart-warning-text').textContent = result.customer_message;
      window.setTimeout(() => document.getElementById('cart-warning').classList.add('show'), 700);
    }
  } catch (error) {
    showAnalysisError(error);
  }
});
