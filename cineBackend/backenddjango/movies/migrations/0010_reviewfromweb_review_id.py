# Generated by Django 5.0 on 2023-12-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_reviewfromweb_made_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewfromweb',
            name='review_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
