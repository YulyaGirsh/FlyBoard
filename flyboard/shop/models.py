from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена', blank=True)
    guarantee = models.IntegerField(verbose_name='Гарантия', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

