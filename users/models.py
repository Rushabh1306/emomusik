from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

from emomusik.settings import BASE_DIR

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'profile_pics')
    emotion_image = models.ImageField(default='profile_pics/download.jpg', upload_to = 'emotion_pics')
    emotion = models.CharField(max_length=20,blank=True,null=True)
    language = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            print(img.height)
            output_size = (300,300)
            img.thumbnail(output_size)
            print(img.height)
            img.save(self.image.path)