# Generated by Django 4.1 on 2023-07-14 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('app_users', '0006_alter_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='menu.categories', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_online',
            field=models.BooleanField(default=False, verbose_name='Он-лайн'),
        ),
        migrations.AddField(
            model_name='users',
            name='stream_key',
            field=models.CharField(max_length=255, null=True, verbose_name='Ключ трансляции'),
        ),
        migrations.AddField(
            model_name='users',
            name='stream_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название трансляции'),
        ),
    ]
