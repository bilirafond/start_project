# Generated by Django 2.0.6 on 2018-09-15 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_many', '0013_auto_20180915_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 15, 9, 54, 30, 107178)),
        ),
    ]
