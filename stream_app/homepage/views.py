from django.shortcuts import render
from django.http import HttpResponseNotFound

from stream_app import settings
from .models import Categories, Menu


def index(request):
    context={
        'title': 'Lastream.online', 
    }

    return render(request, 'index.html', context=context)


def categories(request):
    cats=Categories.objects.all()
    context={
        'cats': cats, 
        'title': 'Категории - Lastream.online', 
        'settings': settings.DEBUG,
    }
    
    return render(request, 'categories.html', context=context)


def show_categories(request, pk):
    cats=Categories.objects.all()
    context={
        'cat_id': pk,
        'cats': cats, 
        'title': 'Категории - Lastream.online', 
        'settings': settings.DEBUG,
    }
    
    return render(request, 'show_cat.html', context=context)


def about(request):
    return render(request, 'about.html', {'title': 'О нас - Lastream.online'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')