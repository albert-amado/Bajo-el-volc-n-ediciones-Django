from django import forms
from django.contrib import admin
from .models import SlideHero
from .models import FraseEditorial
from .models import BannerCarrusel
from .models import PremiosCarrusel


admin.site.register(SlideHero)
admin.site.register(FraseEditorial)
@admin.register(BannerCarrusel)
class BannerCarruselAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)


@admin.register(PremiosCarrusel)
class PremiosCarruselAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)