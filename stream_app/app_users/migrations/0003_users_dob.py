# Generated by Django 4.1 on 2023-04-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_remove_users_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='dob',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
    ]