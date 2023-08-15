from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from studio.key_generate import get_key


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
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.stream_key=get_key(form.cleaned_data['username'])
        self.object.stream_name=f"Трансляция {form.cleaned_data['username']}"
        
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Регистрация - Lastream.online'

        return context


class UserProfile(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        
        return render(request,'profile.html', context={'user_form': user_form,'title':'Профиль - Lastream.online'})
    
    def post(self, request):
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            request.user.save()

        return render(request,'profile.html', context={'user_form': user_form, 'title':'Профиль - Lastream.online'})   


def logout_user(request):
    logout(request)
    
    return redirect ('home')   
