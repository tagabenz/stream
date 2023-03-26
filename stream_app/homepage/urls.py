from django.urls import path

from .views import *


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('categories/', categories, name='categories'),
    path('categories/<int:pk>', show_categories),
    path('about/', about, name='about'),
]