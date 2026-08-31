# views.py
from django.shortcuts import render
from catalogo.models import Libro, Autor
from noticias.models import Noticia
from home.models import SlideHero, BannerCarrusel, PremiosCarrusel

def index(request):
    categoria = request.GET.get('categoria', 'todos')
    generos = dict(Libro.Genero.choices)
    etiquetas = dict(Libro.Etiqueta.choices)

    queryset = Libro.objects.select_related('autor')
    if categoria in generos:
        libros = queryset.filter(genero=categoria)
    elif categoria in etiquetas:
        libros = queryset.filter(etiqueta=categoria)
    else:
        libros = queryset.all()
        categoria = 'todos'

    context = {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente...",
        "libros": libros,
        "categoria_actual": categoria,
        "noticias": Noticia.objects.all().order_by('-fecha')[:4],
        "autores": Autor.objects.all()[:6],
        "banners": BannerCarrusel.objects.filter(activo=True),
        "slides": SlideHero.objects.filter(activo=True).order_by('orden'),
        "premios": PremiosCarrusel.objects.filter(activo=True),
    }
    return render(request, "home/index.html", context)