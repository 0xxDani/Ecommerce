# Generated by Django 4.2.8 on 2024-01-06 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_delete_order_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='status',
            new_name='estado_de_entrega',
        ),
    ]