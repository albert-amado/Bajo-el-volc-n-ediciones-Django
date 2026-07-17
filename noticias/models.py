from django.db import models
from django.utils.text import slugify


class Noticia(models.Model):
    """Sección Noticias/Eventos. 'galeria' del JSON se separa en ImagenGaleria (1:N)."""

    class Categoria(models.TextChoices):
        EVENTO = "EVE", "Evento"
        PROXIMA_PUBLICACION = "PRO", "Próximas publicaciones"
        NUEVOS_AUTORES = "AUT", "Nuevos autores"
        FERIA_LIBRO = "FER", "Feria del libro"
        PRESENTACION_LIBROS = "PRE", "Presentación de libros"
        PREMIO_NOVELA = "PRM", "Premio nacional de novela"

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    resumen = models.TextField()
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="noticias/")
    fecha = models.CharField(
        max_length=50,
        help_text="Texto libre en origen ('Pronto', fechas sueltas). "
        "Migrar a DateField cuando el dato esté normalizado.",
    )
    categoria = models.CharField(max_length=3, choices=Categoria.choices)
    enlace_pdf = models.FileField(upload_to="noticias/pdf/", blank=True, null=True)
    mostrar_participantes = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class ImagenGaleria(models.Model):
    """
    Imágenes de la galería de eventos dentro de una Noticia.
    FK a Noticia (M:1) y FK opcional a Autor (relaciona la foto con el autor).
    'catalogo.Autor' en string: evita import circular entre apps.
    """
    noticia = models.ForeignKey(
        Noticia, on_delete=models.CASCADE, related_name="galeria"
    )
    autor = models.ForeignKey(
        "catalogo.Autor", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="apariciones_galeria"
    )
    src = models.ImageField(upload_to="eventos/")
    titulo = models.CharField(max_length=200)
    libro = models.CharField(
        max_length=200, blank=True,
        help_text="Referencia textual al libro mostrado en la foto"
    )

    class Meta:
        verbose_name = "Imagen de galería"
        verbose_name_plural = "Imágenes de galería"

    def __str__(self):
        return f"{self.noticia.titulo} - {self.titulo}"