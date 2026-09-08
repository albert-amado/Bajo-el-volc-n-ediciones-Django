function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

export async function agregarAlCarrito(libroId) {
  const response = await fetch("/carrito/agregar/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `libro_id=${libroId}`,
  });

  const data = await response.json();

  if (data.ok) {
    actualizarContador(data.total_items);
    mostrarToast(`"${data.titulo}" agregado al carrito`);
  } else {
    mostrarToast("Error al agregar al carrito");
  }

  return data;
}

export function actualizarContador(total) {
  const el = document.getElementById("cartCount");
  if (el) el.textContent = String(total);
}

export function mostrarToast(msg) {
  const t = document.getElementById("bevToast");
  if (!t) return;
  t.textContent = msg;
  t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2600);
}