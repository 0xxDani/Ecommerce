# Generated by Django 4.2.8 on 2023-12-23 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_product_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('RD', 'Ropa Dama'), ('ME', 'Maquillaje'), ('CD', 'Calzado Dama'), ('PD', 'Perfumería Dama'), ('AD', 'Accesorios Dama'), ('PH', 'Productos para el hogar'), ('BS', 'Bolsos'), ('ES', 'Electrodomésticos'), ('JA', 'Juguetería'), ('AE', 'Arte'), ('PL', 'Productos de aplicacion corporal'), ('NP', 'Novedades y promociones'), ('CS', 'Chaquetas'), ('CC', 'Calzado para caballero'), ('AC', 'Accesorios Caballero')], max_length=2),
        ),
    ]