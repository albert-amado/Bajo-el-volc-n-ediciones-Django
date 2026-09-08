from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/<slug:slug>/", views.detalle_libro, name="detalle_libro"),
    path("autores/<int:pk>/", views.detalle_autor, name="detalle_autor"),
]