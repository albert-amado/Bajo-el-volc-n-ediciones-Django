function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}

function getCsrfToken() {
  const input = document.querySelector('[name=csrfmiddlewaretoken]');
  return input ? input.value : getCookie('csrftoken');
}

async function agregarAlCarrito(id) {
  const res = await fetch(window.CARRITO_URLS.agregar, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCsrfToken(),
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `libro_id=${id}`,
  });
  const data = await res.json();
  if (!data.ok) {
    mostrarToast('Error al agregar el libro');
    return;
  }
  actualizarContador(data.total_items);
  mostrarToast(`"${data.titulo}" agregado al carrito`);
}

function actualizarContador(total) {
  const el = document.getElementById('cartCount');
  if (el) el.textContent = String(total);
}

function mostrarToast(msg) {
  const t = document.getElementById('bevToast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2600);
}

document.addEventListener('click', (e) => {
  const btn = e.target.closest('.js-btn-carrito');
  if (!btn) return;
  agregarAlCarrito(btn.dataset.id);
});