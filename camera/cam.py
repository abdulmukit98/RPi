from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

#camera = PiCamera()
#camera.start_preview()
#sleep(5)
#camera.stop_preview()

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)    # input pullup
GPIO.setup(15, GPIO.IN)            # normal, without pullup


switch = GPIO.input(15)

while True:
    if(switch == True):
        camera = PiCamera()
        camera.capture("/home/pi/Desktop/image.jpg")
        print("done")
        break
    
    

