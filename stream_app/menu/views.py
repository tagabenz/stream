from django.shortcuts import render

from .models import Categories
from stream_app import settings


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