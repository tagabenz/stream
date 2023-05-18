from django import forms

from .models import Stream


class StreamForms(forms.ModelForm):
    title=forms.CharField(min_length=1,max_length=255, label='Название трансляции:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Название трансляции"}))
    class Meta():
        model=Stream
        fields=['title','cat']
        widgets={
                'cat': forms.Select(attrs={'class': 'form-select', 'placeholder': "Категория",}),
            }

class StreamSettingsForm(forms.ModelForm):
    stream_key=forms.CharField(label="KEY:", widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark', 'disabled':'', 'type':'password'}))
    class Meta():
        model=Stream
        fields=['stream_key']    