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
            'stream_url': f"rtmp://{settings.OME_HOST}:1935/input"
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
            'stream_url': f"rtmp://{settings.OME_HOST}:1935/input",
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