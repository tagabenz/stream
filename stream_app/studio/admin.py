from django.contrib import admin
from .models import *

@admin.register(Studio)
class Streams(admin.ModelAdmin):
    list_display=('stream_name','stream_key','cat')
    
    