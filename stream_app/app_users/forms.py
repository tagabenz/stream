from django import forms


class AuthForm(forms.Form):
    username=forms.CharField(min_length=3,label="Логин")
    password=forms.CharField(widget=forms.PasswordInput, min_length=8,label="Пароль")