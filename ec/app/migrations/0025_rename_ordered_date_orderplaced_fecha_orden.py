# Generated by Django 4.2.8 on 2023-12-18 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_title_product_titulo_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='ordered_date',
            new_name='fecha_orden',
        ),
    ]
