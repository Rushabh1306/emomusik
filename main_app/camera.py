import cv2
import os
from django.conf import settings
from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json
emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
faceFile = os.path.join(settings.XML_FOLDER,'haarcascade_frontalface_default.xml')
faceDetect=cv2.CascadeClassifier(faceFile)
model_path = settings.MODEL_PATH
model = model_from_json(open(os.path.join(model_path,"fer.json"), "r").read())
model.load_weights(os.path.join(model_path,"fer.h5"))

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        faces=faceDetect.detectMultiScale(frame, 1.3, 5)
        gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        for x,y,w,h in faces:
            x1,y1=x+w, y+h
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 1)
            cv2.line(frame, (x,y), (x+30, y),(255,0,255), 6) #Top Left
            cv2.line(frame, (x,y), (x, y+30),(255,0,255), 6)

            cv2.line(frame, (x1,y), (x1-30, y),(255,0,255), 6) #Top Right
            cv2.line(frame, (x1,y), (x1, y+30),(255,0,255), 6)

            cv2.line(frame, (x,y1), (x+30, y1),(255,0,255), 6) #Bottom Left
            cv2.line(frame, (x,y1), (x, y1-30),(255,0,255), 6)

            cv2.line(frame, (x1,y1), (x1-30, y1),(255,0,255), 6) #Bottom right
            cv2.line(frame, (x1,y1), (x1, y1-30),(255,0,255), 6)

            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image  
            roi_gray=cv2.resize(roi_gray,(48,48))
            #Processes the image and adjust it to pass it to the model
            image_pixels = image.img_to_array(roi_gray)
            image_pixels = np.expand_dims(image_pixels, axis = 0)
            image_pixels /= 255

            predictions = model.predict(image_pixels)
            max_index = np.argmax(predictions[0])
            predicted_emotion = emotions[max_index]  
            cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()