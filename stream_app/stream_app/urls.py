from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from stream_app import settings
from homepage.views import pageNotFound
from blog.views import BlogsListView, BlogsDetailView
from app_users.views import LoginView, UserRegistration, logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('categories/', include('menu.urls')),
    path('blog/', BlogsListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogsDetailView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

 