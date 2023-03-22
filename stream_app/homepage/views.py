# from django.shortcuts import render
# from django.views import View
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Главная страница'

        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')