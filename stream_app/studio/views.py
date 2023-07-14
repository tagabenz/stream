from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .serializers import *
from .key_generate import get_key
from app_users.models import Users
from stream_app import settings


class Studio(View):
    def get(self, request):
        form = StreamForms(instance=request.user)
        form_settings = StreamSettingsForm(instance=request.user)   
        
        return render(request,'studio.html', context={
            'form': form,
            'form_settings': form_settings, 
            'title':'Студия - Lastream.online',
            'stream_url': settings.PULL_URL,
            'output_url': F"{settings.PROTOCOL}://{settings.OME_HOST}:{settings.LLHLS_PORT}/input/{request.user}/llhls.m3u8",
            })
    
    def post(self, request):
        form = StreamForms(request.POST, instance=request.user)
        form_settings = StreamSettingsForm(instance=request.user) 

        if form.is_valid():
            form.save()  

        return render(request,'studio.html', context={
            'form': form,
            'form_settings': form_settings, 
            'title':'Студия - Lastream.online',
            'stream_url': settings.PULL_URL,
            'output_url': F"{settings.PROTOCOL}://{settings.OME_HOST}:{settings.LLHLS_PORT}/input/{request.user}/llhls.m3u8",
            })    
    

class StudioAPIView(APIView):
    def get(self, request, command):
       try:instance=Users.objects.get(username=request.user)
       except:return Response({'error':'Object does not exists'})

       if command=="status_change":
           if instance.is_online:instance.is_online=False
           else:instance.is_online=True
           instance.save()

           return Response(instance.is_online)
    
    def put(self, request, command, *args, **kwargs):
        try:instance=Users.objects.get(username=request.user)
        except:return Response({'error':'Object does not exists'})

        if command=="key_generate":
            serializer=Key_Generate_Serializer(data={'stream_key': get_key(request.user)},instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response(serializer.data)