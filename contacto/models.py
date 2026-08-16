from django.db import models


class MensajeEditorial(models.Model):
    """Mensajes recibidos desde el formulario de contacto público."""
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.asunto} — {self.nombre}"