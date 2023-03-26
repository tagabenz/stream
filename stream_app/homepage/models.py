from django.db import models
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    # def __str__(self):
    #     return self.name
    
    def get_absolute_url(self):
        return reverse('cat_show',kwargs={'pk': self.pk})