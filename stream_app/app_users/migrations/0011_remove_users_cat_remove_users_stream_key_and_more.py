# Generated by Django 4.1 on 2023-10-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0010_remove_users_is_online_users_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='users',
            name='stream_key',
        ),
        migrations.RemoveField(
            model_name='users',
            name='stream_name',
        ),
    ]