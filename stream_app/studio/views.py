from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Stream
from .forms import *
from .serializers import StudioSerializer
from .key_generate import get_key

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
            'stream_url': settings.PULL_URL,
            'output_url': F"{settings.PROTOCOL}://{settings.OME_HOST}:{settings.LLHLS_PORT}/input/{request.user}/llhls.m3u8",
            })
    
    def post(self, request):
        user = Stream.objects.get(autor=request.user)
        form = StreamForms(request.POST, instance=user)
        form_settings = StreamSettingsForm(instance=user) 

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
    def get(self, request):
        w=Stream.objects.all()

        return Response(StudioSerializer(w,many=True).data)
    
    def put(self, request, *args, **kwargs):
        try:instance=Stream.objects.get(autor=request.user)
        except:return Response({'error':'Object does not exists'})

        serializer=StudioSerializer(data={'stream_key': get_key(request.user)},instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)