# Generated by Django 4.1 on 2023-05-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_users_image_alter_users_email_alter_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to='user_img/', verbose_name='Аватар'),
        ),
    ]
