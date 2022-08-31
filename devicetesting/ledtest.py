import RPi.GPIO as GPIO
from time import sleep
led =21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(led, GPIO.HIGH)
    sleep(1)
    GPIO.output(led, GPIO.LOW)
    sleep(1)
    
    
