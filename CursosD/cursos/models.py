from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del curso")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion_horas = models.IntegerField(verbose_name="Duración (horas)")
    modalidad = models.CharField(max_length=50, choices=[("presencial", "Presencial"), ("en línea", "En línea")], verbose_name="Modalidad")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible?")
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True, verbose_name="Imagen del curso")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["creado"]  # Más antigua a más reciente

    def __str__(self):
        return self.nombre
