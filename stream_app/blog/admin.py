from django.contrib import admin
from blog.models import Blogs
# Register your models here.

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    pass 
