from django.shortcuts import render, get_object_or_404
from .models import Noticia


def lista(request):
    return render(request, "noticias/lista.html", {
        "noticias": Noticia.objects.all().order_by('-fecha'),
    })


def detalle(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, "noticias/detalle.html", {
        "noticia": noticia,
    })