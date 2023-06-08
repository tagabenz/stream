from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categories/', CategoriesViews.as_view(), name='categories'),
    path('categories/<slug:cat_slug>', show_categories, name='cat_show'),
]