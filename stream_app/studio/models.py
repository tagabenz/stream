from django.db import models
from menu.models import Categories
from app_users.models import Users


class Stream(models.Model):
    title=models.CharField(max_length=255, verbose_name="Название")
    time_update=models.DateTimeField(auto_now=True, null=True)
    is_online=models.BooleanField(default=False, verbose_name='Он-лайн')
    autor=models.ForeignKey(Users, models.CASCADE, verbose_name='Пользователь', db_index=True )
    cat=models.ForeignKey(Categories, models.PROTECT, verbose_name='Категория',default=1)
    stream_key=models.CharField(max_length=255, null=True,verbose_name="Ключ трансляции")
