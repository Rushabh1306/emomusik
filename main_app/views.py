from django.http import response
from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.contrib.auth.decorators import login_required
import cv2
from main_app.models import Song
from django.conf import settings
from .camera import Video
from .utils import gen

@login_required
def home(request):
    context={}
    context['title']="Home"

    # songs = Song.objects.first()
    # context['item'] = songs

    return render(request,'main_app/home.html',context)


@login_required
def video(request):
    return StreamingHttpResponse(gen(Video()),
    content_type='multipart/x-mixed-replace; boundary=frame')


@login_required
def emotion(request):
    context={}
    context['title']="Emotion Detection"
    if request.POST:
        language = request.POST['language']
        # print(language)
        context['language'] = language
        user = request.user.profile
        user.language = language
        user.save()
    return render(request,'main_app/emotion.html',context)


@login_required      
def playlist(request):
    context={}
    context['title']="Playlist"
    if request.method == 'POST' and request.FILES['emotion_img']:
        emotion = request.POST['emotion']
        emotion_img = request.FILES.get('emotion_img')
        request.user.profile.save()
        user = request.user.profile
        user.emotion = emotion
        user.save()
        songs = Song.objects.filter(language = request.user.profile.language,
                                    emotion = request.user.profile.emotion)
        context['songs'] = songs

    return render(request,'main_app/playlist.html',context)





