# Generated by Django 4.2.6 on 2024-01-01 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authaccounts', '0006_alter_useraccount_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2024, 1, 1)),
        ),
    ]