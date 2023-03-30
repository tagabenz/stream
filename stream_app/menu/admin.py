from django.contrib import admin
from .models import Menu, Categories


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('id','name')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=('id','name')
