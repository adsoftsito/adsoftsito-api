# Generated by Django 4.2.13 on 2024-11-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaveProdServ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveprodserv', models.TextField(blank=True, default='', null=True)),
                ('descripcion', models.TextField(blank=True, default='', null=True)),
                ('sinonimos', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClaveUnidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveunidad', models.TextField(blank=True, default='', null=True)),
                ('nombre', models.TextField(blank=True, default='', null=True)),
                ('descripcion', models.TextField(blank=True, default='', null=True)),
                ('simbolo', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formapago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formapago', models.TextField(blank=True, default='', null=True)),
                ('descripcion', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metodopago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodopago', models.TextField(blank=True, default='', null=True)),
                ('descripcion', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
