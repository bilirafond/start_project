# Generated by Django 2.0.6 on 2018-09-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_many', '0017_auto_20180917_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('professional', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='home_group',
            field=models.CharField(max_length=50),
        ),
    ]