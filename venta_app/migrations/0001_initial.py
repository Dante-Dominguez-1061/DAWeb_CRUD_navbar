# Generated by Django 5.1.2 on 2024-11-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_cliente', models.PositiveSmallIntegerField()),
                ('id_empleado', models.PositiveSmallIntegerField()),
                ('fecha_venta', models.DateField()),
                ('total', models.FloatField()),
                ('impuesto', models.FloatField()),
                ('producto_vendido', models.CharField(max_length=100)),
            ],
        ),
    ]
