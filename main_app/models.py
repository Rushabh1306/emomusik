from django.db import models

# Create your models here.
class Song(models.Model):

    MOOD_CHOICE = (
        ('happy','Happy'),
        ('sad','Sad'),
        ('neutral','Neutral'),
        ('angry','Angry'),
    )
    LANGUAGE_CHOICE = (
        ('english','English'),
        ('hindi','Hindi'),
        ('gujarati','Gujarati'),
        ('marathi','Marathi'),
    )
    
    title= models.TextField()
    artist= models.TextField()
    # image= models.ImageField()


    emotion = models.CharField(max_length=10,choices=MOOD_CHOICE,default='Happy')
    language = models.CharField(max_length=10,choices=LANGUAGE_CHOICE,default='Hindi')
    audio_file = models.FileField(upload_to = 'songs',blank=True,null=True)
    # audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20,null=True)
    # paginate_by = 2

    def __str__(self):
        return self.title
