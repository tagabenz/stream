from django import forms


class AuthForm(forms.Form):
    username=forms.CharField(min_length='3', max_length='20', label="Логин", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин",}))
    password=forms.CharField(min_length='8', max_length='20',label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль",}))