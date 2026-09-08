from django.db import models

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    foto = models.ImageField(upload_to="team/")
    bio = models.TextField()

    class Meta:
        verbose_name = "Miembro del equipo"
        verbose_name_plural = "Equipo"
        ordering = ["id"]

    def __str__(self):
        return f"{self.nombre} ({self.cargo})"