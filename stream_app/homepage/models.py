from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('categories', kwargs={'cat_id': self.pk})