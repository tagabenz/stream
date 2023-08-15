from django.urls import path

from .views import *


urlpatterns = [
    path('blog/', BlogsListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogsDetailView.as_view()),
]


