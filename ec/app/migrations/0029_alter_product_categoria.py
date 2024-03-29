# Generated by Django 4.2.8 on 2023-12-22 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_product_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('RC', 'Ropa casual'), ('ME', 'Maquillaje'), ('CO', 'Calzado'), ('PS', 'Perfumes'), ('RI', 'Ropa interior'), ('AD', 'Accesorios Dama'), ('CS', 'Chaquetas'), ('PH', 'Productos para el hogar'), ('BS', 'Bolsos'), ('ES', 'Electrodomésticos'), ('JA', 'Juguetería'), ('AE', 'Arte'), ('AC', 'Accesorios Caballero'), ('PL', 'Productos de aplicacion corporal'), ('NP', 'Novedades y promociones')], max_length=2),
        ),
    ]
