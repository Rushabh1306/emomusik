# Generated by Django 3.2.7 on 2021-11-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emotion_image',
            field=models.ImageField(default='profile_pics/download.jpg', upload_to='emotion_pics'),
        ),
    ]
