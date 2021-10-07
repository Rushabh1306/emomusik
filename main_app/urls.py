from django.contrib import admin
from django.urls import path,include
from .views import HomeView, home

urlpatterns = [
    path('',home,name = "main_app-home")

    ]