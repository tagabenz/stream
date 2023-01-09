from django.db import models

class Blogs(models.Model):
    title=models.CharField(max_length=1000, verbose_name='Заголовок')
    img_url=models.CharField(max_length=1000,default='')
    description = models.CharField(max_length=1000,default='',verbose_name='Описание')

    def __str__(self):
        return str(f"id:{self.id} {self.title} ")
