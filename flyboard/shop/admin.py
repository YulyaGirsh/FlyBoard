from django.contrib import admin

# Register your models here.
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published')
    list_display_links = ('name', 'id')
    search_fields = ('name',  'price','id')


admin.site.register(Products, ProductsAdmin)

