# Generated by Django 2.0.6 on 2018-09-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_many', '0012_auto_20180908_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
