# Generated by Django 2.2 on 2021-09-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_app', '0017_auto_20210910_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
