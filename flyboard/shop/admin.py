from django.contrib import admin

# Register your models here.
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'category')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'price', 'id')
    list_editable = ('is_published', 'category')
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
