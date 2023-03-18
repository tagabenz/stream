from django.contrib import admin
from django.urls import path

from homepage.views import Index
from blog.views import BlogsListView, BlogsDetailView
from app_profiles.views import UserFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('blog/', BlogsListView.as_view()),
    path('blog/<int:pk>/', BlogsDetailView.as_view()),
    path('register/', UserFormView.as_view())
]
