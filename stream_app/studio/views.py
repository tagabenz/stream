from django.shortcuts import render
from django.views.generic import View


class Studio(View):
    
    def get(self, request):
        context={
        'title': 'Студия - Lastream.online',
        }

        return render(request, 'studio.html', context=context)    
    
    