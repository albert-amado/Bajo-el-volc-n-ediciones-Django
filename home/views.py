from django.shortcuts import render
from catalogo.models import Libro
from noticias.models import Noticia
from home.models import SlideHero, AnuncioPremio

from django.shortcuts import render
from catalogo.models import Libro, Autor
from noticias.models import Noticia
from home.models import SlideHero, AnuncioPremio



def index(request):
    categoria = request.GET.get('categoria', 'todos')

    generos = dict(Libro.Genero.choices)
    etiquetas = dict(Libro.Etiqueta.choices)

    if categoria in generos:
        libros = Libro.objects.filter(genero=categoria)
    elif categoria in etiquetas:
        libros = Libro.objects.filter(etiqueta=categoria)
    else:
        libros = Libro.objects.all()
        categoria = 'todos'

    return render(request, "home/index.html", {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente. Descubre nuestro catálogo de novelas, cuentos y poesía de autores colombianos y latinoamericanos.",
        "libros": libros,
        "categoria_actual": categoria,
        "noticias": Noticia.objects.all().order_by('-fecha'),
        "slides": SlideHero.objects.filter(activo=True).order_by('orden'),
        "premio": AnuncioPremio.objects.filter(activo=True).last(),
    })

def index(request):
    categoria = request.GET.get('categoria', 'todos')

    generos = dict(Libro.Genero.choices)
    etiquetas = dict(Libro.Etiqueta.choices)
    
    # 1. Usamos el queryset optimizado con select_related
    queryset = Libro.objects.select_related('autor')

    if categoria in generos:
        libros = queryset.filter(genero=categoria)
    elif categoria in etiquetas:
        libros = queryset.filter(etiqueta=categoria)
    else:
        libros = queryset.all()
        categoria = 'todos'

    return render(request, "home/index.html", {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente. Descubre nuestro catálogo de novelas, cuentos y poesía de autores colombianos y latinoamericanos.",
        "libros": libros,
        "categoria_actual": categoria,
        # 2. Corregido: ordena por fecha descendente y toma las primeras 4
        "noticias": Noticia.objects.all().order_by('-fecha')[:4],
        "slides": SlideHero.objects.filter(activo=True).order_by('orden'),
        "premio": AnuncioPremio.objects.filter(activo=True).last(),
        "autores": Autor.objects.all()[:6],
    })