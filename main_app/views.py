from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
import cv2
import threading
from django.views.decorators import gzip
from django.contrib.auth.decorators import login_required

from main_app.models import Song
# Create your views here.

@login_required
def home(request):
    context={}
    context['title']="Home"

    songs = Song.objects.first()
    context['item'] = songs
    
    return render(request,'main_app/home.html',context)



@gzip.gzip_page
def HomeView(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return HttpResponse("<h1>Hello</h1>")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update,args=()).start()
    
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        image = self.frame
        _,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')



