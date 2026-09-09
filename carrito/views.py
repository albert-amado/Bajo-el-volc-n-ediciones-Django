from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from catalogo.models import Libro
from django.shortcuts import render


@require_POST
def agregar_al_carrito(request):
    """Agrega un libro a la sesión del carrito. Espera libro_id en POST."""
    libro_id = request.POST.get("libro_id")
    if not libro_id:
        return JsonResponse({"ok": False, "error": "libro_id requerido"}, status=400)

    libro = get_object_or_404(Libro, pk=libro_id)
    carrito = request.session.get("carrito", {})

    libro_id_str = str(libro.id)
    carrito[libro_id_str] = carrito.get(libro_id_str, 0) + 1

    request.session["carrito"] = carrito
    request.session.modified = True

    total_items = sum(carrito.values())

    return JsonResponse({
        "ok": True,
        "libro_id": libro.id,
        "titulo": libro.titulo,
        "cantidad": carrito[libro_id_str],
        "total_items": total_items,
    })


def ver_carrito(request):
    """Muestra el contenido del carrito guardado en sesión."""
    carrito_sesion = request.session.get("carrito", {})

    items = []
    total_valor = 0
    total_libros = 0

    if carrito_sesion:
        libros = Libro.objects.in_bulk(carrito_sesion.keys())
        for libro_id_str, cantidad in carrito_sesion.items():
            libro = libros.get(int(libro_id_str))
            if not libro:
                continue
            subtotal = libro.precio * cantidad
            items.append({
                "libro": libro,
                "cantidad": cantidad,
                "subtotal": subtotal,
            })
            total_valor += subtotal
            total_libros += cantidad

    context = {
        "items": items,
        "total_valor": total_valor,
        "total_libros": total_libros,
    }
    return render(request, "carrito/carrito.html", context)

@require_POST
def eliminar_del_carrito(request):
    libro_id = request.POST.get("libro_id")
    carrito = request.session.get("carrito", {})
    carrito.pop(str(libro_id), None)
    request.session["carrito"] = carrito
    request.session.modified = True
    return JsonResponse({"ok": True, "total_items": sum(carrito.values())})

@require_POST
def vaciar_carrito(request):
    request.session["carrito"] = {}
    request.session.modified = True
    return JsonResponse({"ok": True})