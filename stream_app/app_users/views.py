from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from app_users.forms import *


class LoginView(LoginView):
    form_class=AuthForm
    template_name='login.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Вход - Lastream.online'

        return context
    

class UserRegistration(CreateView):
    form_class=UserForm
    template_name='registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Регистрация - Lastream.online'

        return context


def logout_user(request):
    logout(request)
    
    return redirect ('home')    