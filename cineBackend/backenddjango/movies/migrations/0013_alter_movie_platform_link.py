# Generated by Django 5.0 on 2023-12-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_platform_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='platform_link',
            field=models.CharField(max_length=255),
        ),
    ]
