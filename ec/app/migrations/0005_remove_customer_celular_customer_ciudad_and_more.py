# Generated by Django 4.2.7 on 2023-11-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_mobile_customer_celular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='celular',
        ),
        migrations.AddField(
            model_name='customer',
            name='ciudad',
            field=models.CharField(choices=[('Amazonas', 'Leticia'), ('Antioquia', 'Medellín'), ('Arauca', 'Arauca'), ('Atlántico', 'Barranquilla'), ('Bolívar', 'Cartagena'), ('Boyacá', 'Tunja'), ('Caldas', 'Manizales'), ('Caquetá', 'Florencia'), ('Casanare', 'Yopal'), ('Cauca', 'Popayán'), ('Cesar', 'Valledupar'), ('Chocó', 'Quibdó'), ('Córdoba', 'Montería'), ('Cundinamarca', 'Bogotá, D.C.'), ('Guainía', 'Inírida'), ('Guaviare', 'San José del Guaviare'), ('Huila', 'Neiva'), ('La Guajira', 'Riohacha'), ('Magdalena', 'Santa Marta'), ('Meta', 'Villavicencio'), ('Nariño', 'Pasto'), ('Norte de Santander', 'Cúcuta'), ('Putumayo', 'Mocoa'), ('Quindío', 'Armenia'), ('Risaralda', 'Pereira'), ('San Andrés y Providencia', 'San Andrés'), ('Santander', 'Bucaramanga'), ('Sucre', 'Sincelejo'), ('Tolima', 'Ibagué'), ('Valle del Cauca', 'Cali'), ('Vaupés', 'Mitú'), ('Vichada', 'Puerto Carreño')], default='Bogotá, D.C.', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='departamento',
            field=models.CharField(max_length=200),
        ),
    ]