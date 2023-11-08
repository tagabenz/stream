from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .serializers import *
from .key_generate import get_key
from .models import Studio

from stream_app import settings


class Studio(LoginRequiredMixin,View):
    login_url = "/login"
   
    def get(self, request):
        form = StreamForms(instance=request.user.stream)

        return render(request,'studio.html', context={
            'user': request.user,
            'form': form,
            'title':'Студия - Lastream.online',
            'pull_url': settings.OME_RTMP_INPUT_URL,
            'output_url': f"{settings.OME_LLHLS_STREAMING_HOST}/{settings.OME_APP_NAME}/{request.user}/llhls.m3u8",
            'chat_name': request.user.username
            })
    
    def post(self, request):
        form = StreamForms(request.POST, instance=request.user.stream)

        if form.is_valid():
            form.save()  

        return render(request,'studio.html', context={
            'user': request.user,
            'form': form,
            'title':'Студия - Lastream.online',
            'pull_url': settings.OME_RTMP_INPUT_URL,
            'output_url': f"{settings.OME_LLHLS_STREAMING_HOST}/{settings.OME_APP_NAME}/{request.user}/llhls.m3u8",
            'chat_name': request.user.username
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