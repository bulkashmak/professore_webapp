# Generated by Django 2.1.5 on 2019-01-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190109_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость блюда'),
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Масса блюда'),
        ),
    ]
