from django import forms

from app_users.models import Users


class StreamForms(forms.ModelForm):
    stream_name=forms.CharField(min_length=1,max_length=255, label='Название трансляции:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Название трансляции"}))
    class Meta():
        model=Users
        fields=['stream_name','cat']
        widgets={
                'cat': forms.Select(attrs={'class': 'form-select', 'placeholder': "Категория",}),
            }

class StreamSettingsForm(forms.ModelForm):
    stream_key=forms.CharField(label="KEY:", widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark', 'disabled':'', 'type':'password'}))
    class Meta():
        model=Users
        fields=['stream_key']      