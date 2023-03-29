from django.contrib import admin
from blog.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    pass
