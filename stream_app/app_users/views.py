from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from studio.models import Stream
 

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
        # Create Stream.objects in studio.models for User
        Stream.objects.create(
            title='Трансляция ' + form.cleaned_data['username'],
            autor_id=self.object.id,
            cat_id=1
        )
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Регистрация - Lastream.online'

        return context


class UserProfile(LoginRequiredMixin, View):
    # redirect_field_name='/login'

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
