from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('catalog', shop, name='catalog'),
    path('contact', contact, name='contact')
]
