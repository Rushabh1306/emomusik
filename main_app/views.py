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
from users.models import Profile
from django.core.paginator import Paginator

@login_required
def home(request):
    context={}
    context['title']="Home"
    return render(request,'main_app/emomusik_language.html',context)

@login_required
def video(request):
    video_stream = gen(Video(),request)
    return StreamingHttpResponse(video_stream,
    content_type='multipart/x-mixed-replace; boundary=frame')


@login_required
def emotion(request):
    context={}
    context['title']="Emotion Detection"
    if request.POST:
        language = request.POST['language']
        print(request.POST)
        print(request.FILES)
        context['language'] = language
        user = request.user.profile
        user.language = language
        user.save()
    return render(request,'main_app/emomusik_detect.html',context)


@login_required      
def playlist(request):

    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={}
    context['title']="Playlist"
    context['page_obj']=page_obj

    # songs = Song.objects.filter(language = request.user.profile.language,
    #                             emotion = request.user.profile.emotion)
    songs = Song.objects.all()
    context['songs'] = songs
    print(songs)
    print(request.user)
    return render(request,'main_app/new_playlist.html',context)





