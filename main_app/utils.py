import time

def gen(camera,request):
    while True:
        frame=camera.get_frame(request)
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame[0] +
         b'\r\n\r\n')