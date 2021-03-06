# Generated by Django 2.2 on 2021-08-31 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_app', '0004_auto_20210831_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funame', models.CharField(max_length=255)),
                ('goal', models.CharField(max_length=255)),
                ('registry_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registry_created', to='wedding_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='registryone',
            name='registry_owner1',
        ),
        migrations.RemoveField(
            model_name='registrythree',
            name='registry_owner3',
        ),
        migrations.RemoveField(
            model_name='registrytwo',
            name='registry_owner2',
        ),
        migrations.DeleteModel(
            name='Registryfour',
        ),
        migrations.DeleteModel(
            name='Registryone',
        ),
        migrations.DeleteModel(
            name='Registrythree',
        ),
        migrations.DeleteModel(
            name='Registrytwo',
        ),
    ]
