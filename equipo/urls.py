from django.urls import path
from . import views

app_name = "equipo"

urlpatterns = [
    path("nosotros/", views.nosotros, name="nosotros"),
]