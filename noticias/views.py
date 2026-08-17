from django.shortcuts import render, get_object_or_404
from .models import Noticia


def lista(request):
    noticias = Noticia.objects.all().order_by("-fecha")
    categorias = Noticia.Categoria.choices
    return render(request, "noticias/listado.html", {
        "noticias": noticias,
        "categorias": categorias,
    })


def detalle(request, slug):
    noticia = get_object_or_404(
        Noticia.objects.prefetch_related(
            "albumes__multimedia",
            "participacion_set__autor",
            "participacion_set__etiqueta",
        ),
        slug=slug,
    )
    return render(request, "noticias/noticia_detalle.html", {
        "noticia": noticia,
    })