from django import forms
from .models import Stream


class StreamForms(forms.Form):
    class Meta():
        model=Stream
        fields='__all__'