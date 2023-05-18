from django.shortcuts import render
from django.views import View

from .models import Stream
from .forms import *
from stream_app import settings


class Studio(View):
    def get(self, request):
        user = Stream.objects.get(autor=request.user)
        form = StreamForms(instance=user)
        form_settings = StreamSettingsForm(instance=user)
        return render(request,'studio.html', context={
            'form': form,
            'form_settings': form_settings, 
            'title':'Студия - Lastream.online',
            'stream_url': f"rtmp://{settings.OME_HOST}:1935/input"
            })
    
    def post(self, request):
        user = Stream.objects.get(autor=request.user)
        form = StreamForms(request.POST, instance=user)

        if form.is_valid():
            form.save()  

        return render(request,'studio.html', context={
            'form': form,
            'title':'Студия - Lastream.online'
            })    