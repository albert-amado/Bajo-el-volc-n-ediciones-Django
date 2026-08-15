from django.shortcuts import render
from .models import MiembroEquipo


def nosotros(request):
    equipo = MiembroEquipo.objects.all()
    return render(request, "equipo/nosotros.html", {"equipo": equipo})