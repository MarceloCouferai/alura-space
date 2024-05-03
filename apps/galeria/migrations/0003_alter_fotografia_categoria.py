# Generated by Django 5.0.4 on 2024-04-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Nebulosa', 'Nebulosa'), ('Estrela', 'Estrela'), ('Galáxia', 'Galáxia'), ('Planeta', 'Planeta')], default='', max_length=100),
        ),
    ]