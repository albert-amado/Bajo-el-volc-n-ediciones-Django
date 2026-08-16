from django.contrib import admin
from .models import MensajeEditorial


@admin.register(MensajeEditorial)
class MensajeEditorialAdmin(admin.ModelAdmin):
    list_display = ("asunto", "nombre", "correo", "fecha_creacion", "leido")
    list_filter = ("leido", "fecha_creacion")
    search_fields = ("nombre", "correo", "asunto", "mensaje")
    list_editable = ("leido",)
    readonly_fields = ("fecha_creacion",)
    ordering = ("-fecha_creacion",)

    fieldsets = (
        ("Remitente", {"fields": ("nombre", "correo")}),
        ("Mensaje", {"fields": ("asunto", "mensaje")}),
        ("Estado", {"fields": ("leido", "fecha_creacion")}),
    )