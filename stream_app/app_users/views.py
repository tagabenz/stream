from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app_users.forms import *


class LoginView(View):

    def get(self,request):
        form=AuthForm()
        context={
        'form': form,
        'title' : "Вход - Lastream.online",
        }

        return render(request,'login.html',context=context)

    def post(self,request):
        form=AuthForm(request.POST)
        context={
        'form': form,
        'title' : "Вход - Lastream.online",
        }

        if form.is_valid():
            print(form.cleaned_data)

        return render(request,'login.html',context=context)   
    
    
class UserRegistration(CreateView):
    form_class=UserForm
    template_name='registration.html'
    success_url = reverse_lazy('login')