import { agregarAlCarrito } from './carrito.js';

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("addToCartBtn");

  button?.addEventListener("click", () => {
    const id = Number(button.getAttribute("data-id") || "0");
    const titulo = button.getAttribute("data-titulo") || "";
    const precio = Number(button.getAttribute("data-precio") || "0");
    if (id && titulo) {
      agregarAlCarrito(id, titulo, precio);
    }
  });
});