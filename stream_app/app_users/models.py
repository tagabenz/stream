from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    GENDERS=(
        ('М','Мужской'),
        ('Ж','Женский'),
    ) 

    gender = models.CharField(max_length=1,choices=GENDERS,verbose_name='Пол',default='Мужской')
    dob = models.DateField(null=True, verbose_name='Дата рождения')
    email=models.EmailField(unique=True)
    image=models.ImageField(null=True, upload_to="user_img/", verbose_name="Аватар")