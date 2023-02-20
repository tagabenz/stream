from django.contrib import admin
from django.urls import path

from homepage.views import Index, Player
from blog.views import BlogsListView, BlogsDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('player/', Player.as_view()),
    path('blog/', BlogsListView.as_view()),
    path('blog/<int:pk>/', BlogsDetailView.as_view())
]
