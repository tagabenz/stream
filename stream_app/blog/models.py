from django.db import models

class Blogs(models.Model):
    title=models.CharField(max_length=255, null=True)
    img=models.ImageField(upload_to="photos/%Y/%n/%d", null=True)
    content=models.TextField(blank=True, null=True)
    time_create=models.DateTimeField(auto_now_add=True, null=True)
    time_update=models.DateTimeField(auto_now=True, null=True)
    is_published=models.BooleanField(default=True, null=True)

    def __str__(self):
        return str(f"id:{self.id} {self.title} ")
