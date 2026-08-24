from django.shortcuts import render, get_object_or_404
from .models import Autor, Libro


def detalle_autor(request, pk):
    """Ficha de un autor con el listado de sus obras, en una sola consulta."""
    autor = get_object_or_404(
        Autor.objects.prefetch_related("libros"),
        pk=pk,
    )
    return render(request, "catalogo/autor_detalle.html", {
        "autor": autor,
    })


def lista_libros(request):
    """Catálogo general de libros, optimizado con select_related."""
    libros = Libro.objects.select_related("autor").all()

    return render(request, "catalogo/lista_libros.html", {
        "libros": libros,
    })


def detalle_libro(request, slug):
    """Ficha de un libro individual buscado por slug."""
    libro = get_object_or_404(
        Libro.objects.select_related("autor"),
        slug=slug,
    )
    context = {
        "libro": libro,
        "autor": libro.autor,
    }
    return render(request, "catalogo/libro_detalle.html", context)