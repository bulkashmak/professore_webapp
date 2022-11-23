from django.contrib import admin
from preferences.admin import PreferencesAdmin
from django.contrib.sites.models import Site
from .models import *
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


@admin.register(Dish)
class DishAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Dish

    list_display = ('dish_name', 'dish_category', 'dish_subcategory', 'dish_price',)
    list_editable = ('dish_price',)
    list_filter = ('dish_category', 'dish_subcategory',)


class SubCategoryInline(SortableInlineAdminMixin, admin.StackedInline):
    model = SubCategory
    extra = 1


class FotosInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Foto
    extra = 1


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Category
    inlines = [SubCategoryInline, ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    model = Album
    inlines = [FotosInline, ]

# Register your models here.


class PrPreferencesAdmin(PreferencesAdmin):
    model = PrPreferences


admin.site.register(PrPreferences, PrPreferencesAdmin)
admin.site.unregister(Site)