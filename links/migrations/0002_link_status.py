# Generated by Django 4.2.13 on 2025-01-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
