from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView

from stream_app import settings
from .models import Categories


class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Lastream.online'

        return context


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