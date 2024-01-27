from django.urls import path

from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('api/v1/subscriptions', UsersAPIView.as_view(), name="subscriptions"),
    path('api/v1/subscribe/<int:pk>', UsersAPIUpdate.as_view(), name="subscribe")
]