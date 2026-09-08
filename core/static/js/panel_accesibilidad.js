document.addEventListener("DOMContentLoaded", () => {
  const html = document.documentElement;

  const btnModoOscuro = document.getElementById("btnModoOscuro");
  const btnModoGrises = document.getElementById("btnModoGrises");
  const btnAgrandarTexto = document.getElementById("btnAgrandarTexto");
  const btnRestablecer = document.getElementById("btnRestablecer");

  // Aplica el estado guardado al cargar la página
  function aplicarEstadoInicial() {
    const tema = localStorage.getItem("bev-tema");
    if (tema) {
      html.setAttribute("data-bs-theme", tema);
    } else {
      // Fallback a preferencia del sistema si no hay localStorage
      const prefiereOscuro = window.matchMedia("(prefers-color-scheme: dark)").matches;
      html.setAttribute("data-bs-theme", prefiereOscuro ? "dark" : "light");
    }

    if (localStorage.getItem("bev-grises") === "true") {
      html.classList.add("modo-grises");
    }
    if (localStorage.getItem("bev-texto-grande") === "true") {
      html.classList.add("texto-accesible");
    }
  }

  // Alterna claro/oscuro usando el atributo nativo de Bootstrap
  btnModoOscuro.addEventListener("click", () => {
    const actual = html.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
    html.setAttribute("data-bs-theme", actual);
    localStorage.setItem("bev-tema", actual);
  });

  // Alterna escala de grises
  btnModoGrises.addEventListener("click", () => {
    const activo = html.classList.toggle("modo-grises");
    localStorage.setItem("bev-grises", activo);
  });

  // Alterna tamaño de texto aumentado
  btnAgrandarTexto.addEventListener("click", () => {
    const activo = html.classList.toggle("texto-accesible");
    localStorage.setItem("bev-texto-grande", activo);
  });

  // Restablece todo a valores por defecto
  btnRestablecer.addEventListener("click", () => {
    html.removeAttribute("data-bs-theme");
    html.classList.remove("modo-grises", "texto-accesible");
    localStorage.removeItem("bev-tema");
    localStorage.removeItem("bev-grises");
    localStorage.removeItem("bev-texto-grande");
  });

  aplicarEstadoInicial();
});