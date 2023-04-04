from django.urls import path

from .views import *


urlpatterns = [
    path('', UserFormView.as_view(), name='registration'),
]