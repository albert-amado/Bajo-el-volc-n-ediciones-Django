from django.shortcuts import render
from catalogo.models import Libro
from noticias.models import Noticia


def index(request):
    return render(request, "home/index.html", {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente. Descubre nuestro catálogo de novelas, cuentos y poesía de autores colombianos y latinoamericanos.",
        "libros": Libro.objects.all(),
        "slides": Libro.objects.exclude(imagen_hero="").exclude(imagen_hero__isnull=True),
        "noticias": Noticia.objects.all().order_by('-fecha'),
    })