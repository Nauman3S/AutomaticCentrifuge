from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
def startCamera():
    global camera
    camera.start_preview()
    

def stopCamera():
    global camera
    camera.stop_preview()