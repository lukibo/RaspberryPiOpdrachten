#bron powerpoint van Hardware Interfacing periode 6 les 2
import RPi.GPIO as GPIO
import time

LED_PIN6 = 6
LED_PIN13 = 13
BTN_PIN19 = 19
BTN_PIN26 = 26
flashtime = 700
lasttime = 0

ledstatus = [GPIO.LOW, GPIO.LOW]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN6, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BTN_PIN19, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BTN_PIN26, GPIO.IN, GPIO.PUD_DOWN)


def millis():
    return time.time() * 1000

#als de schakelaar is ingedrukt gaat een led knipperen voor 0.7 seconde
while True:
    buttonState = GPIO.input(BTN_PIN26)
    currenttime = millis()
    if buttonState == GPIO.HIGH:
        if(currenttime - lasttime >= flashtime):
            lasttime = currenttime
            if ledstatus[0] == GPIO.HIGH:
                ledstatus[0] = GPIO.LOW
            else:
                ledstatus[0] = GPIO.HIGH
            GPIO.output(LED_PIN13, ledstatus[0])