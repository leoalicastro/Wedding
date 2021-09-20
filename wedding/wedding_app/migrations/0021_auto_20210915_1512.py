# Generated by Django 2.2 on 2021-09-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_app', '0020_auto_20210915_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users_who_like',
        ),
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='wedding_app.User'),
        ),
    ]
