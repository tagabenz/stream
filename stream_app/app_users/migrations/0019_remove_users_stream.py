# Generated by Django 4.1 on 2023-11-22 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0018_remove_users_follow_users_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='stream',
        ),
    ]
