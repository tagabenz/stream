from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from stream_app import settings
from homepage.views import pageNotFound
from blog.views import BlogsListView, BlogsDetailView
from app_profiles.views import UserFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('blog/', BlogsListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogsDetailView.as_view()),
    path('register/', UserFormView.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

 