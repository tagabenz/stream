from django.db import models

from menu.models import Categories
from app_users.models import Users


class Studio(models.Model):
    stream_name = models.CharField(max_length=255, verbose_name="Название трансляции", null=True)
    stream_key = models.CharField(max_length=255, verbose_name="Ключ трансляции", null=True)
    author = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    cat = models.ForeignKey(Categories, models.PROTECT, verbose_name='Категория', default=1)

    def __str__(self):
        return self.stream_name
    
    class Meta():
        verbose_name = "Трансляции"
        verbose_name_plural = "Трансляции"