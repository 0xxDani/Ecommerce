# Generated by Django 4.2.8 on 2024-01-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_orderplaced_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('indicativo', models.CharField(max_length=5)),
                ('identificacion', models.CharField(max_length=20)),
                ('tipo_caso', models.CharField(max_length=20)),
                ('asunto', models.CharField(max_length=200)),
                ('numero_factura', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
