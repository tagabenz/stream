from django import forms


class AuthForm(forms.Form):
    username=CharField()
    password=CharField(widget=forms.PasswordInput)