#bron Jeremy
import RPi.GPIO as GPIO
import time

raspPinnen = [13, 19]
vorigeTijd = 0
status = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(raspPinnen[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(raspPinnen[1], GPIO.OUT)

def millis():
    return time.time() * 1000

#functie die de status van de pinnen regelt
while True:
    if GPIO.input(raspPinnen[0]):
        if millis() - vorigeTijd >= 1000:
            vorigeTijd = millis()
            if status:
                GPIO.output(raspPinnen[1], GPIO.HIGH)
                status = False
            else:
                GPIO.output(raspPinnen[1], GPIO.LOW)
                status = True