from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.PositiveSmallIntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    foto = models.ImageField() 

    def __str__(self):
        return self.nombres