# Generated by Django 2.1.5 on 2019-01-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190111_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['sorting2'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='sorting2',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]
