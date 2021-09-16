import os
import subprocess
def startCamera():
    subprocess.call(["sh", "/home/pi/AutomaticCentrifuge/Firmware/cameraLive.sh"], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

def stopCamera():
    subprocess.call(["sh", "/home/pi/AutomaticCentrifuge/Firmware/stopCamera.sh.sh"], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

