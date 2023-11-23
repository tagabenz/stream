from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView 
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import timedelta

import jwt

from .forms import *

from studio.models import Studio
from studio.key_generate import get_key


class LoginView(LoginView):
    redirect_authenticated_user = True
    form_class = AuthForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        response = HttpResponseRedirect(self.get_success_url())

        response.set_cookie('token', jwt.encode({"sub": self.request.user.username }, key='secret', algorithm="HS256"),max_age=timedelta(days=30))
        
        return response

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход - Lastream.online'
        
        return context


class UserRegistration(CreateView):
    form_class = UserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.slug = form.cleaned_data['username']
        stream = Studio.objects.create(stream_key=get_key(form.cleaned_data['username']),
                                    stream_name=f"Трансляция {form.cleaned_data['username']}",
                                    author=self.object
                                    )
        # self.object.stream = stream
        stream.save()

        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация - Lastream.online'

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
    response = HttpResponseRedirect(reverse("home"))
    response.delete_cookie('token')
    
    return response
