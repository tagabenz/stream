from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categories/', CategoriesViews.as_view(), name='categories'),
    path('categories/<slug:cat_slug>', CategoriesSort.as_view(), name='show_categories'),
    path('<slug:user_slug>/', UserPage.as_view(), name='userpage'),
] 