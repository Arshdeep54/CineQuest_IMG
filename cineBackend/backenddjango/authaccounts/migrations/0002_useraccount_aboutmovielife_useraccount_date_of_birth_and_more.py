# Generated by Django 5.0 on 2023-12-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='aboutmovieLife',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'others')], default='O', max_length=255),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]
