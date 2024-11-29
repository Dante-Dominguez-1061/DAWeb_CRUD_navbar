# Generated by Django 5.1.2 on 2024-11-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_proveedor', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fecha_envio', models.DateField()),
            ],
        ),
    ]