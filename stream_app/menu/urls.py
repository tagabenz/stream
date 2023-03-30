from django.urls import path

from .views import *


urlpatterns = [
    path('', categories, name='categories'),
    path('<int:pk>', show_categories, name='cat_show'),
]