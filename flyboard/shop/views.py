from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Category


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
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {'title': 'Каталог', 'goods': goods, 'categories': categories})


def get_category(request, category_id):
    goods = Products.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.object.get(pk=category_id)
    return render((request, 'shop/category.html', {'goods': goods, 'categories': categories, 'category': category}))
