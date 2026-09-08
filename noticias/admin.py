# noticias/admin.py
from django.contrib import admin
from django.contrib import messages
from .models import Noticia
from .models import AlbumGaleria
from .models import MultimediaGaleria
from .models import EtiquetaRol
from .models import Participacion
from .forms import AlbumAdminForm

EXT_IMAGEN = (".jpg", ".jpeg", ".png", ".webp", ".gif")
EXT_VIDEO = (".mp4", ".mov", ".avi", ".webm")
EXT_DOCUMENTO = (".pdf", ".docx", ".doc", ".xlsx", ".pptx")


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
    form = AlbumAdminForm
    list_display = ("titulo", "noticia", "libro", "autor")
    list_filter = ("noticia",)
    inlines = [MultimediaGaleriaInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        archivos = request.FILES.getlist("archivos_multiples")
        for archivo in archivos:
            nombre = archivo.name.lower()

            if nombre.endswith(EXT_IMAGEN):
                MultimediaGaleria.objects.create(
                    album=obj,
                    tipo=MultimediaGaleria.Tipo.IMAGEN,
                    imagen=archivo,
                    titulo_o_descripcion=archivo.name,
                )
            elif nombre.endswith(EXT_VIDEO):
                MultimediaGaleria.objects.create(
                    album=obj,
                    tipo=MultimediaGaleria.Tipo.VIDEO,
                    video_archivo=archivo,
                    titulo_o_descripcion=archivo.name,
                )
            elif nombre.endswith(EXT_DOCUMENTO):
                MultimediaGaleria.objects.create(
                    album=obj,
                    tipo=MultimediaGaleria.Tipo.DOCUMENTO,
                    archivo_documento=archivo,
                    titulo_o_descripcion=archivo.name,
                )
            else:
                self.message_user(
                    request,
                    f"'{archivo.name}' no se subió: extensión no reconocida.",
                    level=messages.WARNING,
                )


@admin.register(EtiquetaRol)
class EtiquetaRolAdmin(admin.ModelAdmin):
    list_display = ("nombre", "color_css")
    search_fields = ("nombre",)