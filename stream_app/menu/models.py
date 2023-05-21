from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name="Меню"
        verbose_name_plural="Меню"
        ordering=['id']


class Categories(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name='URL')
    img = models.ImageField(upload_to="svg/", null=True)

    def get_absolute_url(self):
        return reverse('cat_show',kwargs={'post_slug': self.slug})
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name="Категории"
        verbose_name_plural="Категории"
        ordering=['id']
    