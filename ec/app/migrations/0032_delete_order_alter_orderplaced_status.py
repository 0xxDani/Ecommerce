# Generated by Django 4.2.8 on 2024-01-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Aceptado', 'Aceptado'), ('Empacado', 'Empacado'), ('En camino', 'En camino'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado'), ('Pendiente', 'Pendiente')], default='Pending', max_length=50),
        ),
    ]