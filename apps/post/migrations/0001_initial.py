# Generated by Django 4.0 on 2021-12-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posteos',
            },
        ),
    ]
