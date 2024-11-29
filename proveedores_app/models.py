from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id_proveedor = models.PositiveSmallIntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_envio = models.DateField()

    def __str__(self):
        return self.nombre