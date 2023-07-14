from typing import Any, Dict

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from menu.models import Categories
from app_users.models import Users


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
    model=Users
    template_name='categories.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title']='Категории - Lastream.online'

        return context

    def get_queryset(self):
        
        return Users.objects.filter(is_online=True)
    

class CategoriesSort(ListView):
    model=Users
    template_name='categories.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title']='Категории - Lastream.online'

        return context
    
    def get_queryset(self):
        
        return Users.objects.filter(is_online=True, cat__slug=self.kwargs['cat_slug'])