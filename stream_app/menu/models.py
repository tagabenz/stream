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
    menu = models.ForeignKey('Menu', on_delete=models.PROTECT, null=True)
    
    def get_absolute_url(self):
        return reverse('cat_show',kwargs={'pk': self.pk})
    
    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name="Категории"
        verbose_name_plural="Категории"
        ordering=['id']


class MenuItem(models.Model):
    name=models.CharField(max_length=50)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    def __str__(self) -> str:
        return self.name
    
    