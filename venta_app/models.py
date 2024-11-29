from django.db import models

# Create your models here.

class Venta(models.Model):
    id_venta = models.PositiveSmallIntegerField(primary_key=True)
    id_cliente = models.PositiveSmallIntegerField()
    id_empleado = models.PositiveSmallIntegerField()
    fecha_venta = models.DateField()
    total = models.FloatField()
    impuesto = models.FloatField()
    producto_vendido = models.CharField(max_length=100)

    def __str__(self):
        return self.producto_vendido