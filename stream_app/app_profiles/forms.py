from django import forms


class UserForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()