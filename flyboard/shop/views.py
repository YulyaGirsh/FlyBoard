from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html', {'Title': 'Главная'})


def contact(request):
    return render(request, 'shop/contact.html',{'Title': 'Контакты'})


def shop(request):
    return render(request, 'shop/shop.html',{'Title': 'Каталог'})
