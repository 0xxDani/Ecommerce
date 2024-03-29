# Generated by Django 4.2.8 on 2023-12-14 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'Carrito de compras'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Administradores'},
        ),
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'verbose_name_plural': 'Pedidos Realizados'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': 'Pagos'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name_plural': 'Lista de seguimiento'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discounted_price',
            new_name='precio_con_descuento',
        ),
    ]
