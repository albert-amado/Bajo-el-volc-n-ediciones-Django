# models.py
from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class PremiosCarrusel(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="premios_carrusel/")
    enlace_url = models.URLField(blank=True)
    archivo_pdf = models.FileField(upload_to="premios_carrusel/pdfs/", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    texto_boton = models.CharField(max_length=50, blank=True)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Banner de Premios Carrusel"
        verbose_name_plural = "Banners de Premios Carrusel"
        ordering = ["orden", "-id"]

    def __str__(self):
        return f"{self.orden} - {self.titulo}"
class SlideHero(models.Model):
    titulo_interno = models.CharField(max_length=100)
    imagen_fondo = models.ImageField(upload_to="home/hero/")
    documento_descarga = models.FileField(upload_to="home/hero/documentos/", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slide del Carrusel Hero"
        verbose_name_plural = "Slides del Carrusel Hero"
        ordering = ["orden"]

    def __str__(self):
        return self.titulo_interno    

class FraseEditorial(models.Model):
    mensaje = models.TextField()
    autor = models.CharField(max_length=150, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Frase Editorial"
        verbose_name_plural = "Frases Editoriales"

    def __str__(self):
        return self.mensaje[:50]

class BannerCarrusel(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="carrusel/")
    enlace_url = models.URLField(blank=True)
    archivo_pdf = models.FileField(upload_to="carrusel/pdfs/", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    texto_boton = models.CharField(max_length=50, blank=True)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Banner del carrusel"
        verbose_name_plural = "Banners del carrusel"
        ordering = ["orden", "-id"]

    def __str__(self):
        return f"{self.orden} - {self.titulo}"