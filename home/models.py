from django.db import models

class AnuncioPremio(models.Model):
    frase = models.CharField(
        max_length=255,
        help_text="Frase principal del recuadro de premio o anuncio."
    )
    color_fondo = models.CharField(
        max_length=7,
        default="#000000",
        help_text="Código hexadecimal del color de fondo. Ej: #FF5733"
    )
    imagen = models.ImageField(
        upload_to="home/premios/",
        help_text="Imagen obligatoria del anuncio."
    )
    documento_pdf = models.FileField(
        upload_to="home/premios/pdf/",
        blank=True,
        null=True,
        help_text="Archivo PDF opcional adjunto al anuncio."
    )
    activo = models.BooleanField(
        default=True,
        help_text="Desmarcar para ocultar el anuncio sin borrarlo."
    )

    class Meta:
        verbose_name = "Anuncio de Premio"
        verbose_name_plural = "Anuncios de Premios"

    def __str__(self):
        return self.frase

class SlideHero(models.Model):
    titulo_interno = models.CharField(
        max_length=100, 
        help_text="Solo para identificar el slide en el panel de administración. No se mostrará en la web."
    )
    imagen_fondo = models.ImageField(
        upload_to="home/hero/",
        help_text="Imagen de fondo obligatoria del slide."
    )
    documento_descarga = models.FileField(
        upload_to="home/hero/documentos/",
        blank=True,
        null=True,
        help_text="Archivo o documento opcional para descarga."
    )
    etiqueta = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Texto corto opcional sobre la imagen. Ej: Nuevo, Preventa, Evento."
    )
    orden = models.PositiveIntegerField(
        default=0,
        help_text="Número que define el orden de aparición en el carrusel. Menor número aparece primero."
    )
    activo = models.BooleanField(
        default=True,
        help_text="Desmarcar para ocultar el slide sin borrarlo."
    )

    class Meta:
        verbose_name = "Slide del Carrusel Hero"
        verbose_name_plural = "Slides del Carrusel Hero"
        ordering = ["orden"]

    def __str__(self):
        return self.titulo_interno    
class FraseEditorial(models.Model):
    mensaje = models.TextField(
        help_text="Mensaje o frase inspiradora de la editorial."
    )
    autor = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Nombre de quién firma la frase. Opcional."
    )
    activo = models.BooleanField(
        default=True,
        help_text="Desmarcar para ocultar la frase sin borrarla."
    )

    class Meta:
        verbose_name = "Frase Editorial"
        verbose_name_plural = "Frases Editoriales"

    def __str__(self):
        return self.mensaje[:50]