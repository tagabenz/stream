# Generated by Django 4.1 on 2023-04-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('img', models.ImageField(null=True, upload_to='photos/%Y/%n/%d')),
                ('content', models.TextField(blank=True, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
