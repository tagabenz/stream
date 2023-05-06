from django.urls import path

from .views import *


urlpatterns = [
    path('', Studio.as_view(), name='studio'),
]


