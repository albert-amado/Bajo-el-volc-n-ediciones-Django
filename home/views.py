from django.shortcuts import render
from catalogo.models import Libro
from noticias.models import Noticia
from home.models import SlideHero, AnuncioPremio


def index(request):
    return render(request, "home/index.html", {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente. Descubre nuestro catálogo de novelas, cuentos y poesía de autores colombianos y latinoamericanos.",
        "libros": Libro.objects.all(),
        "noticias": Noticia.objects.all().order_by('-fecha'),
        "slides": SlideHero.objects.filter(activo=True).order_by('orden'),
        "premio": AnuncioPremio.objects.filter(activo=True).last(),
    })