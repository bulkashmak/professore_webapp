# Generated by Django 2.1.5 on 2019-01-09 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dish_price',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_weight',
        ),
    ]