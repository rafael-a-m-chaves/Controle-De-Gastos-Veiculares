# Generated by Django 3.1.7 on 2021-05-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_myuser_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='cargo',
            field=models.CharField(default='Motorista;Administrador;Propietario', max_length=150),
        ),
    ]
