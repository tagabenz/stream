from django.contrib import admin
from .models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=('pk','username',)
    prepopulated_fields= {"slug":("username",)}