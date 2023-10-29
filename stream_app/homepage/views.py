from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView

from stream_app import settings
from menu.models import Categories
from app_users.models import Users
from studio.models import Studio
from .utils import DataMixin


def index(request):
    context={
        'title': 'Lastream.online',
    }

    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html', {'title': 'О нас - Lastream.online'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class CategoriesViews(DataMixin, ListView):
    model = Users
    template_name = 'categories.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return Users.objects.filter(username__in=self.get_stream_list())
    

class CategoriesSort(DataMixin, ListView):
    model = Users
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()

        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        
        return Users.objects.filter(username__in=self.get_stream_list(), cat__slug=self.kwargs['cat_slug'])


class UserPage(DetailView):
    model = Users
    template_name = 'userpage.html'
    slug_url_kwarg = 'user_slug'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output_url'] = f"{settings.OME_LLHLS_STREAMING_HOST}/{settings.OME_APP_NAME}/{self.object}/llhls.m3u8"
        context['title'] = f"{self.object} - Lastream.online"
        
        return context