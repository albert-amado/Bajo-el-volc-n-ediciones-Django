from django.db import models
from django.core.exceptions import ValidationError
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Noticia(models.Model):
    class Categoria(models.TextChoices):
        EVENTO = "evento", "Evento"
        LANZAMIENTO = "lanzamiento", "Lanzamiento"
        CONVOCATORIA = "convocatoria", "Convocatoria"
        ENTREVISTA = "entrevista", "Entrevista"
        PREMIO = "premio", "Premio"

    titulo = models.CharField(max_length=200, default="Sin título", blank=False)
    slug = models.SlugField(max_length=220, unique=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    fecha = models.DateField()
    resumen = models.CharField(max_length=300, default="Sin resumen", blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="noticias/portadas/", blank=True, null=True)
    enlace_pdf = models.URLField(blank=True, null=True)
    participantes = models.ManyToManyField(
        "catalogo.Autor",
        through="Participacion",
        related_name="noticias_participadas",
        blank=True,
    )

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo


class AlbumGaleria(models.Model):
    """Agrupación explícita de multimedia por evento/tema dentro de una noticia."""
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="albumes")
    titulo = models.CharField(max_length=200)
    libro = models.CharField(max_length=200, blank=True, null=True)
    autor = models.ForeignKey("catalogo.Autor", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Álbum de galería"
        verbose_name_plural = "Álbumes de galería"
        ordering = ["id"]

    def __str__(self):
        return f"{self.titulo} ({self.noticia.titulo})"

class MultimediaGaleria(models.Model):
    class Tipo(models.TextChoices):
        IMAGEN = "imagen", "Imagen"
        VIDEO = "video", "Video"
        DOCUMENTO = "documento", "Documento"

    album = models.ForeignKey(AlbumGaleria, on_delete=models.CASCADE, related_name="multimedia")
    tipo = models.CharField(max_length=15, choices=Tipo.choices)

    imagen = models.ImageField(upload_to="noticias/galeria/imagenes/", blank=True, null=True)
    video_archivo = models.FileField(upload_to="noticias/galeria/videos/", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    video_url = models.URLField(blank=True, null=True)
    archivo_documento = models.FileField(upload_to="noticias/galeria/documentos/", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    titulo_o_descripcion = models.CharField(max_length=200, blank=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Elemento multimedia"
        verbose_name_plural = "Elementos multimedia"
        ordering = ["orden"]

    def __str__(self):
        return f"{self.get_tipo_display()} — {self.titulo_o_descripcion or self.album.titulo}"

    def clean(self):
        if self.tipo == self.Tipo.IMAGEN:
            if not self.imagen:
                raise ValidationError({"imagen": "Debes subir una imagen para el tipo 'Imagen'."})
            self.video_archivo = None
            self.video_url = ""
            self.archivo_documento = None

        elif self.tipo == self.Tipo.VIDEO:
            if not self.video_archivo and not self.video_url:
                raise ValidationError("Debes subir un archivo de video o proporcionar una URL para el tipo 'Video'.")
            self.imagen = None
            self.archivo_documento = None

        elif self.tipo == self.Tipo.DOCUMENTO:
            if not self.archivo_documento:
                raise ValidationError({"archivo_documento": "Debes subir un archivo para el tipo 'Documento'."})
            self.imagen = None
            self.video_archivo = None
            self.video_url = ""
class EtiquetaRol(models.Model):
    """Rol o etiqueta asignable a un participante en una noticia (ej. 'Invitado especial')."""
    nombre = models.CharField(max_length=100, unique=True)
    color_css = models.CharField(
        max_length=30,
        blank=True,
        help_text="Nombre de variable CSS o clase para el color del badge (ej. 'bev-gray-1500').",
    )

    class Meta:
        verbose_name = "Etiqueta de rol"
        verbose_name_plural = "Etiquetas de rol"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Participacion(models.Model):
    """Tabla puente: qué Autor participó en qué Noticia, con qué rol."""
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    autor = models.ForeignKey("catalogo.Autor", on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(EtiquetaRol, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Participación"
        verbose_name_plural = "Participaciones"
        unique_together = ["noticia", "autor"]

    def __str__(self):
        return f"{self.autor} en {self.noticia} ({self.etiqueta or 'sin rol'
    })"