from django.shortcuts import render
from django.views import View

from app_users.forms import AuthForm


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