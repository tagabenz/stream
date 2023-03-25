from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView


menu=['Игры','Общение','Кино']


class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Lastream.online'

        return context


def categories(request):
    return render(request, 'categories.html', {'menu': menu, 'title': 'Категории - Lastream.online'})

def about(request):
    return render(request, 'about.html', {'title': 'О нас - Lastream.online'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')