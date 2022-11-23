# Generated by Django 2.1.5 on 2019-01-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190111_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prpreferences',
            options={'verbose_name': 'Настройки сайта', 'verbose_name_plural': 'Настройки сайта'},
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='admin_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта для получения заявок на бронирования'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='fb_link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на Фейсбук'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='fs_link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на Forsquare'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='ig_link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на Инстаграм'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='tel1',
            field=models.CharField(blank=True, max_length=200, verbose_name='Телефон №1'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='tel2',
            field=models.CharField(blank=True, max_length=200, verbose_name='Телефон №2'),
        ),
        migrations.AddField(
            model_name='prpreferences',
            name='working_time',
            field=models.CharField(blank=True, max_length=200, verbose_name='Время работы'),
        ),
    ]