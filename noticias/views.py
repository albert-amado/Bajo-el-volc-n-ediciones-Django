from django.shortcuts import render, get_object_or_404
from .models import Noticia


def listado(request):
    return render(request, "noticias/listado.html", {
        "noticias": Noticia.objects.all(),
        "categorias": Noticia.Categoria.choices,
    })


def detalle(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, "noticias/detalle.html", {"noticia": noticia})