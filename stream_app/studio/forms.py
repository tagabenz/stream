from django import forms

from studio.models import Studio


class StreamForms(forms.ModelForm):
    stream_name=forms.CharField(min_length=1,max_length=255, label='Название трансляции:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Название трансляции"}))
    
    class Meta():
        model = Studio
        fields = ['stream_name','cat']
        widgets = {
                'cat': forms.Select(attrs={'class':'form-select', 'placeholder':"Категория",}),
            }