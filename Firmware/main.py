from ledStripHandler import *
from motorDriverHandler import *
from camHandler import *
import time

ledState('white')#idle state
#startCamera()


tm=0

while 1:
    try:
        if(isMotorRunning()):
            time.sleep(1)#use 1 second as a freq handler
            servoAngle=0
            ledState('green')
            if(tm<5 and servoAngle<90):#motor picks up the speed and servo gradually moves to 90 degrees
                #SetServoAngle(servoAngle)
                tm=tm+1
                #servoAngle=servoAngle+18
            if(tm>=5):
                print('servo at 90 and motor at full speed')
                tm=tm+1
                if(tm>=10):#stays on for 10 second
                    stopMotors()
                    if(servoAngle>1):
                        ledState('blue')#or purple
                        #servoAngle=servoAngle-1
                        #SetServoAngle(servoAngle)#gradually coming to angle 0 degrees
                    else:
                        tm=0
                        stopMotors()#stop everything
                        #SetServoAngle(0)
                        ledState('white')
    except Exception as e:
        print('e',e)

try:
    ##clean exit
    p1.stop()
    p2.stop()
    p.stop()
    GPIO.cleanup()
    #stopCamera()                
except Exception as e:
    print('Clean exit,e:',e)