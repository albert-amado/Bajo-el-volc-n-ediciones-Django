from django import forms
from django.contrib import admin
from .models import AnuncioPremio
from .models import SlideHero
from .models import FraseEditorial
from .models import BannerCarrusel


class AnuncioPremioForm(forms.ModelForm):
    class Meta:
        model = AnuncioPremio
        fields = "__all__"
        widgets = {
            "color_fondo": forms.TextInput(
                attrs={"type": "color", "style": "height: 40px; width: 60px; cursor: pointer;"}
            ),
        }


@admin.register(AnuncioPremio)
class AnuncioPremioAdmin(admin.ModelAdmin):
    form = AnuncioPremioForm


admin.site.register(SlideHero)
admin.site.register(FraseEditorial)
@admin.register(BannerCarrusel)
class BannerCarruselAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)