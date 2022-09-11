# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Школа стрима | Главная страница'

        return context
