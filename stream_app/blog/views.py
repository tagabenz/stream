from django.views.generic import ListView, DetailView
from blog.models import Blogs


class BlogsListView(ListView):
    model = Blogs
    template_name='blog.html'
    content_object_name='blogs_list'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Блог'

        return context


class BlogsDetailView(DetailView):
    model=Blogs
    template_name='blog_detail.html'
