from django.shortcuts import render

from app_users.forms import AuthForm


def login_view(request):
    if request.method == "POST":
        form=AuthForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=AuthForm()
    
    context={
        'form': form,
        'title' : "Вход - Lastream.online",
    }

    return render(request,'login.html',context=context)