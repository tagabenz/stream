# Generated by Django 4.1 on 2023-07-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_alter_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(default='/user_img/login_img.png', null=True, upload_to='user_img/', verbose_name='Аватар'),
        ),
    ]
