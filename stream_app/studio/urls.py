from django.urls import path

from .views import *


urlpatterns = [
    path('studio/', Studio.as_view(), name='studio'),
]