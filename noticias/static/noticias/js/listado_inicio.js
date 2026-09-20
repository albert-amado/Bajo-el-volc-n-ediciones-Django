document.addEventListener("DOMContentLoaded", function () {
  const carrusel = document.getElementById("noticiasCarrusel");
  const btnPrev = document.getElementById("noticiasPrev");
  const btnNext = document.getElementById("noticiasNext");
  if (!carrusel || !btnPrev || !btnNext) return;

  const distancia = 344; // 320px tarjeta + 24px gap

  btnPrev.addEventListener("click", () =>
    carrusel.scrollBy({ left: -distancia, behavior: "smooth" })
  );
  btnNext.addEventListener("click", () =>
    carrusel.scrollBy({ left: distancia, behavior: "smooth" })
  );
});