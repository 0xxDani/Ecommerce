# Generated by Django 4.2.8 on 2023-12-18 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_ordered_date_orderplaced_fecha_orden'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='valor_total',
        ),
    ]