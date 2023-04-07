from django import forms
from django.core.exceptions import ValidationError

from app_profiles.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields='__all__'
        widgets = {}
        for m in User._meta.get_fields():
            widgets[m.name] = forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Логин",})
            
    def clean_login(self):
        login=self.cleaned_data['login']
        if len(login)<3:
            raise ValidationError("Минимум 3 символа")
        
        return login
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise ValidationError("Минимум 8 символа")
        
        return password
    
    def clean_first_name(self):
        first_name=self.cleaned_data['first_name']
        if len(first_name)<3:
            raise ValidationError("Минимум 3 символа")
        
        return first_name
    
    def clean_last_name(self):
        last_name=self.cleaned_data['last_name']
        if len(last_name)<3:
            raise ValidationError("Минимум 3 символа")
        
        return last_name