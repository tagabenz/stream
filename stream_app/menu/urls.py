from django.urls import path

from .views import *


urlpatterns = [
    path('categories/', categories, name='categories'),
    path('<slug:post_slug>', show_categories, name='cat_show'),
]