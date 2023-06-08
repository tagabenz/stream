from typing import Any, Dict

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from studio.models import Stream
from menu.models import Categories


cats=Categories.objects.all()


def index(request):
    context={
        'title': 'Lastream.online',
    }

    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html', {'title': 'О нас - Lastream.online'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class CategoriesViews(ListView):
    model=Stream
    template_name='categories.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['cats']=cats
        context['title']='Категории - Lastream.online'

        return context

    def get_queryset(self):
        
        return Stream.objects.filter(is_online=True)
    

def show_categories(request, cat_slug):
    cats=Categories.objects.all()
    context={
        'cat_id': cat_slug,
        'cats': cats, 
        'title': 'Категории - Lastream.online',
    }
    
    return render(request, 'show_cat.html', context=context)    