# Generated by Django 3.2.7 on 2021-10-07 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211007_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
    ]
