from django.urls import path

from .views import *


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('categories/', categories),
    path('about/', about),
]