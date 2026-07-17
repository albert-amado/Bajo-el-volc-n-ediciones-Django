from django.shortcuts import render
from django.templatetags.static import static


def index(request):
    return render(request, "home/index.html", {
        "page_title": "Bajo el Volcán Editorial Literaria",
        "description": "Editorial literaria independiente. Descubre nuestro catálogo de novelas, cuentos y poesía de autores colombianos y latinoamericanos.",
        "image": static("img/ui/logo.webp"),
        "static_logo": static("img/ui/logo.webp"),
    })