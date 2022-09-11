from django.views.generic import TemplateView

class Index(TemplateView):
    template_name='blog.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Школа стрима | Блог'
        context['name']='Hfpsdasdo g'
        return context
