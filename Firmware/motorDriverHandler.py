#This programe used to demonstare how to use Loch Antiphase with Hat-MDD10
#AN pin will act as sterring to control direction
#DIG pin will act to ON/OFF motor output.
import signal
import sys
import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG2 = 24				# set dir2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat
START_BUTTON_GPIO = 27
STOP_BUTTON_GPIO = 17
IR_SENSOR_GPIO = 22
LED_RED = 19
LED_GREEN = 6
LED_BLUE = 5
servoPIN = 4

p1=None
p2=None
p=None
dcMotorRunning=0
def ledState(v):
    if(v=='red'):
        GPIO.output(LED_RED,GPIO.HIGH) #LED will be switched ON
        GPIO.output(LED_GREEN,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_BLUE,GPIO.LOW) #LED will be switched OFF
    if(v=='white'):
        GPIO.output(LED_RED,GPIO.HIGH) #LED will be switched ON
        GPIO.output(LED_GREEN,GPIO.HIGH) #LED will be switched OFF
        GPIO.output(LED_BLUE,GPIO.HIGH) #LED will be switched OFF

    elif(v=='green'):
        GPIO.output(LED_RED,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_GREEN,GPIO.HIGH) #LED will be switched ON
        GPIO.output(LED_BLUE,GPIO.LOW) #LED will be switched OFF
    elif(v=='blue'):
        GPIO.output(LED_RED,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_GREEN,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_BLUE,GPIO.HIGH) 
    elif(v=='off'):
        GPIO.output(LED_RED,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_GREEN,GPIO.LOW) #LED will be switched OFF
        GPIO.output(LED_BLUE,GPIO.LOW) 
def SetServoAngle(angle):
    global p

    duty = angle / 18 + 2

    GPIO.output(servoPIN, True)

    p.ChangeDutyCycle(duty)

    sleep(1)

    GPIO.output(servoPIN, False)

    p.ChangeDutyCycle(0)

def startMotors():
    global p1,p2
    GPIO.output(AN1, GPIO.HIGH)		# set AN1 as HIGH, M1B will turn ON
    GPIO.output(AN2, GPIO.HIGH)		# set AN2 as HIGH, M2B will turn ON
    p1.start(0)				# set Direction for M1
    p2.start(0)				# set Direction for M2  
    
def stopMotors():
    global p1,p2
    GPIO.output(AN1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
    GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
    p1.start(0)                          # Direction can ignore
    p2.start(0)    
def backwardMotors():
    global p1,p2
    GPIO.output(AN1, GPIO.HIGH)       
    GPIO.output(AN2, GPIO.HIGH)       
    p1.start(100)                     
    p2.start(0)  

def startTheMotor(channel):
    global dcMotorRunning
    ledState('green')
    startMotors()
    dcMotorRunning=1
def stopTheMotors(channel):
    global dcMotorRunning
    stopMotors()
    dcMotorRunning=0

def isMotorRunning():
    global dcMotorRunning
    return dcMotorRunning

GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
GPIO.setup(START_BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(START_BUTTON_GPIO, GPIO.BOTH, callback=startTheMotor, bouncetime=100)
GPIO.setup(STOP_BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(STOP_BUTTON_GPIO, GPIO.BOTH, callback=stopTheMotors, bouncetime=100)
GPIO.setup(IR_SENSOR_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(IR_SENSOR_GPIO, GPIO.BOTH, callback=startTheMotor, bouncetime=100)
GPIO.setup(LED_RED, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_BLUE, GPIO.OUT, initial= GPIO.LOW)
p = GPIO.PWM(servoPIN, 50) # GPIO 4 for PWM with 50Hz
p.start(0) # Initialization
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(DIG1, 100)		# set pwm for M1
p2 = GPIO.PWM(DIG2, 100)		# set pwm for M2


# p.stop()
# GPIO.cleanup()