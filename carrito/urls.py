from django.urls import path
from . import views

app_name = "carrito"

urlpatterns = [
    path("agregar/", views.agregar_al_carrito, name="agregar"),
    path("eliminar/", views.eliminar_del_carrito, name="eliminar"),
    path("vaciar/", views.vaciar_carrito, name="vaciar"),
    path("", views.ver_carrito, name="ver"),
]