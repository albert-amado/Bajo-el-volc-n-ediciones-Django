from django.urls import path
from . import views

app_name = "noticias"

urlpatterns = [
    path("", views.lista, name="listado"),
    path("<slug:slug>/", views.detalle, name="detalle"),
]