from django.db import models
from preferences.models import Preferences
from tinymce.models import HTMLField

TYPES = (
    ('d', 'Еда'),
    ('b', 'Напиток'),
)


class PrPreferences(Preferences):
    about_us_text = HTMLField(blank=True, verbose_name='Текст о нас (HTML)')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес в подвале')
    address_in_contacts = models.CharField(max_length=200, blank=True, verbose_name='Адрес в контактах')
    tel1 = models.CharField(max_length=200, blank=True, verbose_name='Телефон №1')
    tel2 = models.CharField(max_length=200, blank=True, verbose_name='Телефон №2')
    working_time = models.CharField(max_length=200, blank=True, verbose_name='Время работы')
    fb_link = models.CharField(max_length=200, blank=True, verbose_name='Ссылка на Фейсбук')
    ig_link = models.CharField(max_length=200, blank=True, verbose_name='Ссылка на Инстаграм')
    fs_link = models.CharField(max_length=200, blank=True, verbose_name='Ссылка на Forsquare')
    admin_email = models.EmailField(blank=True, verbose_name='Электронная почта для получения заявок на бронирования')
    slides_speed = models.IntegerField(default=2000, blank=True, verbose_name='Скорость смены фоновых слайдов (в мс)')
    index_meta_desc = models.TextField(blank=True, verbose_name='Тег meta-description главной страницы')
    contacts_meta_desc = models.TextField(blank=True, verbose_name='Тег meta-description страницы с контактами')
    booking_meta_desc = models.TextField(blank=True, verbose_name='Тег meta-description страницы с формой бронирования стола')

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'


class Category(models.Model):
    sorting = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')
    category_name = models.CharField(max_length=200, blank=False, verbose_name='Наименование категории')
    category_description = models.TextField(blank=True, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['sorting']

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sorting = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')
    subcategory_name = models.CharField(max_length=200, blank=False, verbose_name='Наименование подкатегории')
    subcategory_description = models.TextField(blank=True, verbose_name='Описание подкатегории')

    subcategory_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Родительская категория',
        related_name='category_subcategories',
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['sorting']

    def __str__(self):
        name = self.subcategory_name
        if self.subcategory_category:
            name += ' / ' + self.subcategory_category.category_name
        return name


class Dish(models.Model):
    sorting = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')
    # published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    dish_name = models.CharField(max_length=200, blank=False, verbose_name='Наименование блюда (рус.)')
    dish_eng_name = models.CharField(max_length=200, blank=True, verbose_name='Наименование блюда (англ.)')
    dish_price = models.IntegerField(blank=True, null=True, verbose_name='Цена блюда')
    dish_description = models.TextField(blank=True, null=True, verbose_name='Описание блюда')
    dish_weight = models.IntegerField(blank=True, null=True, verbose_name='Масса блюда')
    dish_type = models.CharField(max_length=1, choices=TYPES, verbose_name='Тип блюда', default='d', blank=False)

    dish_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория блюда',
        related_name='category_dishes',
    )

    dish_subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Подкатегория блюда',
        related_name='subcategory_dishes',

    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['sorting']

    def __str__(self):
        return self.dish_name


class Album(models.Model):
    album_name = models.CharField(max_length=200, blank=True, verbose_name='Название альбома')

    class Meta:
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбомы'

    def __str__(self):
        if self.album_name:
            name = self.album_name
        else:
            name = 'Альбом без названия №%s' % self.id
        name += ' (%s фотографий)' % str(self.album_fotos.count())
        return name


class Foto(models.Model):
    sorting = models.IntegerField(blank=True, default=0, verbose_name='Сортировка')
    foto_name = models.CharField(max_length=200, blank=True, verbose_name='Название фотографии')
    foto_img = models.ImageField(blank=True, upload_to='images', verbose_name='Фотография')

    foto_album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Альбом фотографии',
        related_name='album_fotos'
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['sorting']

    # Create your models here.
