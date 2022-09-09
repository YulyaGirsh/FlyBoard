from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


# Create your views here.
def index(request):

    # res = '<h1>Список новостей </h1>'
    # for item in goods:
    #     res+=f'<div> {item.name}<div/>\n'
    # return HttpResponse(res)
    return render(request, 'shop/index.html', {'title': 'Главная', })


def contact(request):
    return render(request, 'shop/contact.html', {'title': 'Контакты'})


def shop(request):
    goods = Products.objects.all()
    return render(request, 'shop/shop.html', {'title': 'Каталог', 'goods': goods})
