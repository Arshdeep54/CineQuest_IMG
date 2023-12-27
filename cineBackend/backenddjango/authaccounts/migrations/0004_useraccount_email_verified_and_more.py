# Generated by Django 5.0 on 2023-12-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authaccounts', '0003_alter_useraccount_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='verification_otp',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
