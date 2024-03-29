from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    GENDERS=(
        ('М','Мужской'),
        ('Ж','Женский'),
    ) 

    gender = models.CharField(max_length=1, choices=GENDERS, verbose_name='Пол', default='Мужской')
    dob = models.DateField(null=True, verbose_name='Дата рождения')
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, upload_to="user_img/", default="/user_img/login_img.png", verbose_name="Аватар")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    following = models.ManyToManyField('self', related_name='followers', blank=True, symmetrical=False)

    def get_absolute_url(self):
        return reverse('userpage',kwargs={'user_slug': self.slug})