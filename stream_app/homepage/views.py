from typing import Any

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from stream_app import settings
from menu.models import Categories
from app_users.models import Users

from requests.auth import HTTPBasicAuth
import requests,json


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
        context['output_url']=settings.OUTPUT_URL

        return context

    def get_queryset(self):
        online_streams=requests.get(f"{settings.PROTOCOL}://oven:8081/v1/vhosts/default/apps/input/streams", auth=HTTPBasicAuth(settings.OME_API_TOKEN[0], settings.OME_API_TOKEN[1])).json()['response']

        return Users.objects.filter(username__in=online_streams)
    

class CategoriesSort(ListView):
    model=Users
    template_name='categories.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title']='Категории - Lastream.online'
        context['output_url']=settings.OUTPUT_URL
        
        return context
    
    def get_queryset(self):
        online_streams=requests.get(f"{settings.OME_API_URL}/vhosts/default/apps/input/streams", auth=HTTPBasicAuth(settings.OME_API_TOKEN[0], settings.OME_API_TOKEN[1])).json()['response']
        
        return Users.objects.filter(username__in=online_streams, cat__slug=self.kwargs['cat_slug'])