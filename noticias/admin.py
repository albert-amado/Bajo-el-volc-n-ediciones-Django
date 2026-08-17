from django.contrib import admin
from .models import Noticia, AlbumGaleria, MultimediaGaleria, EtiquetaRol, Participacion


class MultimediaGaleriaInline(admin.TabularInline):
    model = MultimediaGaleria
    extra = 1
    fields = ("tipo", "imagen", "video_archivo", "video_url", "archivo_documento", "titulo_o_descripcion", "orden")


class AlbumGaleriaInline(admin.StackedInline):
    model = AlbumGaleria
    extra = 0
    fields = ("titulo", "libro", "autor")
    show_change_link = True


class ParticipacionInline(admin.TabularInline):
    model = Participacion
    extra = 1
    autocomplete_fields = ["autor"]


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha")
    list_filter = ("categoria", "fecha")
    search_fields = ("titulo", "resumen", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
    inlines = [AlbumGaleriaInline, ParticipacionInline]


@admin.register(AlbumGaleria)
class AlbumGaleriaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "noticia", "libro", "autor")
    list_filter = ("noticia",)
    inlines = [MultimediaGaleriaInline]


@admin.register(EtiquetaRol)
class EtiquetaRolAdmin(admin.ModelAdmin):
    list_display = ("nombre", "color_css")
    search_fields = ("nombre",)