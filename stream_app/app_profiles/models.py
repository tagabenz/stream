from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20,verbose_name='Логин')
    password = models.CharField(max_length=20,verbose_name='Пароль')
    first_name = models.CharField(max_length=20,verbose_name='Имя')
    last_name = models.CharField(max_length=20,verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    dob = models.DateField(verbose_name='Дата рождения')


