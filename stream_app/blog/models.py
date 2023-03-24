from django.db import models

class Blogs(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to="photos/%Y/%n/%d")
    content=models.TextField(blank=True)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return str(f"id:{self.id} {self.title} ")
