from django.shortcuts import render

from app_users.forms import AuthForm


# Create your views here.
def login_view(request):
    auth_form=AuthForm()
    context={
        'form': auth_form
    }

    return render(request,'login.html',context=context)