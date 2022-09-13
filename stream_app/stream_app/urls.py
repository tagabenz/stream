from django.contrib import admin
from django.urls import path

from homepage.views import Index
from blog.views import BlogsListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('blog/', BlogsListView.as_view())
]
