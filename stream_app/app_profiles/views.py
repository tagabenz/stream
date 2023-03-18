from django.shortcuts import render
from django.views import View
from app_profiles.forms import UserForm

# Create your views here.
class UserFormView(View):

    def get(self, request):
        user_form=UserForm()
        return render(request, 'register.html', context={'user_form': user_form})