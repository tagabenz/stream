from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Users


class AuthForm(AuthenticationForm):
    username=forms.CharField(min_length='3', max_length='20', label="Логин", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин",}))
    password=forms.CharField(min_length='8', max_length='20',label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль",}))


class UserForm(UserCreationForm):
    username=forms.CharField(min_length='3', max_length='20', label="Логин", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин",}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email",}))
    first_name=forms.CharField(min_length='3', max_length='20', label="Имя", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Имя",}))
    last_name=forms.CharField(min_length='3', max_length='20', label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Фамилия",}))
    dob=forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': "Дата рождения",}))
    password1=forms.CharField(min_length='8', max_length='20', label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль",}))
    password2=forms.CharField(min_length='8', max_length='20', label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Подтверждение пароля",}))
    
    class Meta():
        model=Users
        fields=('username','email','first_name','last_name','gender','dob','password1','password2')
        widgets={
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': "Пол",}),
        }