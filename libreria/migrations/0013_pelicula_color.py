# Generated by Django 4.1 on 2023-04-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0012_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='color',
            field=models.BooleanField(default=False, null=True, verbose_name='Color'),
        ),
    ]