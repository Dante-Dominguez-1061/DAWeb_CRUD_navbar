from django.db import models

# Create your models here.

class Videojuego(models.Model):
    id_videojuego = models.PositiveSmallIntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    compañia = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha_lanzamiento = models.DateField()
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.titulo