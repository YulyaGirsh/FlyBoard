from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog', shop, name='catalog'),
    path('contact', contact, name='contact'),
    # path('category/<int:category_id/>', get_category)
]
