# Generated by Django 2.2 on 2021-09-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_app', '0009_auto_20210901_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedding',
            name='cdate',
            field=models.DateField(),
        ),
    ]
