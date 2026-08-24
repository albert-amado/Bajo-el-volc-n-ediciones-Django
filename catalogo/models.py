from django.db import models
from django.utils.text import slugify

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to="autores/", blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True, help_text="URL completa del perfil de Instagram")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    @property
    def obtener_iniciales(self):
        if not self.nombre:
            return ""
        palabras = self.nombre.split()
        return "".join(palabra[0] for palabra in palabras[:2]).upper()

    @property
    def instagram_username(self):
        if not self.instagram_url:
            return ""
        return self.instagram_url.rstrip("/").split("/")[-1]

class Libro(models.Model):
    """
    Catálogo de libros. FK a Autor (M:1) porque el JSON original
    ya normaliza esta relación vía 'libros_ids' en autores.json.
    """

    class Formato(models.TextChoices):
        FISICO = "FIS", "Libro Físico"

    class Genero(models.TextChoices):
        NOVELA = "NOV", "Novela"
        CUENTOS = "CUE", "Cuentos"
        MISTERIO = "MIS", "Misterio"
        ROMANCE = "ROM", "Romance"
        CRIMEN = "CRI", "Crimen"

    class Etiqueta(models.TextChoices):
        DESTACADO = "DES", "Destacado"
        NUEVO = "NUE", "Nuevo"
        PREVENTA = "PRE", "Preventa"

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.PROTECT, related_name="libros"
    )
    genero = models.CharField(max_length=3, choices=Genero.choices)
    formato = models.CharField(
        max_length=3, choices=Formato.choices, default=Formato.FISICO
    )
    editorial = models.CharField(max_length=150, default="Bajo el Volcán")
    precio = models.PositiveIntegerField(help_text="Precio en COP, sin decimales")
    anio = models.PositiveSmallIntegerField()
    idioma = models.CharField(max_length=50, default="Español")
    dimensiones = models.CharField(max_length=50, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    paginas = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="libros/")
    etiqueta = models.CharField(max_length=3, choices=Etiqueta.choices, blank=True)
    descripcion = models.TextField()
    frase = models.TextField(blank=True, help_text="Cita destacada del libro")
    separador = models.BooleanField(
        default=False, help_text="Equivale a 'Si'/'No'/'' del JSON original"
    )
    nuevo = models.BooleanField(default=False)
    destacado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-anio", "titulo"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo