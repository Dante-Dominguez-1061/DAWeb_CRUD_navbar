from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleado = models.PositiveSmallIntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sueldo = models.FloatField()
    puesto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres