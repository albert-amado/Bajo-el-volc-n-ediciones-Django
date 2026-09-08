from django.urls import path
from . import views

app_name = "carrito"

urlpatterns = [
    path("agregar/", views.agregar_al_carrito, name="agregar"),
    path("", views.ver_carrito, name="ver"),
]