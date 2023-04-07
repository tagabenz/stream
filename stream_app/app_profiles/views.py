from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from app_profiles.forms import UserForm
from app_profiles.models import User


class UserFormView(View):
    
    def get(self, request):
        user_form=UserForm()
        context={
            'user_form': user_form,
            'title' : "Регистрация - Lastream.online",
        }

        return render(request, 'registration.html', context=context)
    
    def post(self, request):
        user_form=UserForm(request.POST)
        context={
            'user_form': user_form,
            'title' : "Регистрация - Lastream.online",
        }
        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        
        return render(request, 'registration.html', context={'user_form': user_form})    
