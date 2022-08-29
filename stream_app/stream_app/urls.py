from django.contrib import admin
from django.urls import path
from homepage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
]
