from RPi.GPIO import GPIO 
from time import sleep 
GPIO.setmode(GPIO.Board)
GPIO.setup(8 , GPIO.OUT , initial = GPIO.LOW)

while True:
    GPIO.output(8 , GPIO.HIGH )
    sleep(1)
    GPIO.output(8 , GPIO.LOW)
    sleep(1)