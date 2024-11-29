# Generated by Django 5.1 on 2024-11-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('id_consola', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('precio', models.PositiveSmallIntegerField()),
                ('fecha_lanzamiento', models.DateField()),
                ('compañia', models.CharField(max_length=100)),
                ('stock', models.PositiveSmallIntegerField()),
            ],
        ),
    ]