from django.contrib import admin
from django.urls import path,include
from .views import emotion, home, playlist, video

urlpatterns = [
    path('',home,name = "main_app-home"),
    path('emotion',emotion,name = "main_app-emotion"),
    path('playlist',playlist,name = "main_app-playlist"),
    path('video',video,name = "main_app-video")

    ]