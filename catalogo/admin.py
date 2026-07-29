from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad")
    search_fields = ("nombre", "nacionalidad")
    list_filter = ("nacionalidad",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "genero",
        "formato",
        "precio",
        "anio",
        "etiqueta",
        "nuevo",
        "destacado",
    )
    list_filter = ("genero", "formato", "etiqueta", "nuevo", "destacado", "anio")
    search_fields = ("titulo", "autor__nombre", "isbn", "editorial")
    prepopulated_fields = {"slug": ("titulo",)}  # genera el slug automáticamente al escribir el título
    autocomplete_fields = ("autor",)  # útil cuando hay muchos autores
    list_editable = ("precio", "nuevo", "destacado")  # edición rápida desde la lista