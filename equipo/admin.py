from django.contrib import admin
from .models import MiembroEquipo

@admin.register(MiembroEquipo)
class MiembroEquipoAdmin(admin.ModelAdmin):
    # Campos que se verán en la tabla principal del admin
    list_display = ("nombre", "cargo")
    
    # Campos que permiten búsqueda
    search_fields = ("nombre", "cargo")
    
    # Opcional: si quieres que la biografía sea un área de texto más amplia, 
    # Django ya lo hace por defecto con TextField, pero si necesitas 
    # un control más específico podrías usar:
    # readonly_fields = ("id",)