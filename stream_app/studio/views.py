from django.shortcuts import render
from django.views import View

from .models import Stream
from .forms import StreamForms


class Studio(View):
    def get(self, request):
        user = Stream.objects.get(autor=request.user)
        form = StreamForms(instance=user)
       
        return render(request,'studio.html', context={'form': form,'title':'Студия - Lastream.online'})
    
    def post(self, request):
        user = Stream.objects.get(autor=request.user)
        form = StreamForms(request.POST, instance=user)

        if form.is_valid():
            form.save()  

        return render(request,'studio.html', context={'form': form,'title':'Студия - Lastream.online'})    