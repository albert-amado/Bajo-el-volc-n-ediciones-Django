import { CheckoutMessenger } from './checkoutMessenger.js';

function getCsrfToken() {
  const input = document.querySelector('[name=csrfmiddlewaretoken]');
  return input ? input.value : null;
}

function getItems() {
  const el = document.getElementById('cartData');
  return el ? JSON.parse(el.textContent) : [];
}

async function eliminarDelCarrito(id) {
  const res = await fetch(window.CARRITO_URLS.eliminar, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCsrfToken(),
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `libro_id=${id}`,
  });
  const data = await res.json();
  if (data.ok) window.location.reload();
}

async function vaciarCarrito() {
  const res = await fetch(window.CARRITO_URLS.vaciar, {
    method: 'POST',
    headers: { 'X-CSRFToken': getCsrfToken() },
  });
  const data = await res.json();
  if (data.ok) window.location.reload();
}

document.addEventListener('click', (e) => {
  const removeBtn = e.target.closest('.bev-btn-remove');
  if (removeBtn) {
    eliminarDelCarrito(removeBtn.dataset.id);
    return;
  }

  if (e.target.closest('#clearCart')) {
    vaciarCarrito();
    return;
  }

  if (e.target.closest('#buyWhatsApp')) {
    new CheckoutMessenger().openWhatsApp(getItems());
    return;
  }

  if (e.target.closest('#buyEmail')) {
    new CheckoutMessenger().openEmail(getItems());
  }
});