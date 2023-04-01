from django.contrib import admin
from .models import *

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('id','name','url')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=('id','name','slug')
    prepopulated_fields= {"slug":("name",)}