from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    GENDERS=(
        ('М','Мужской'),
        ('Ж','Женский'),
    ) 

    gender = models.CharField(max_length=1,choices=GENDERS,verbose_name='Пол',default='Мужской')
    dob = models.DateField(null=True, verbose_name='Дата рождения')