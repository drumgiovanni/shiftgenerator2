# Generated by Django 2.0.4 on 2018-04-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djsg', '0002_auto_20180420_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='mail',
            field=models.CharField(max_length=95, unique=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='w_num',
            field=models.CharField(max_length=23, unique=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='worker_fname',
            field=models.CharField(max_length=95, unique=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='worker_name',
            field=models.CharField(max_length=95, unique=True),
        ),
    ]