#bron powerpoint van Hardware Interfacing periode 6 les 2
import RPi.GPIO as GPIO
import time

LED_PIN6 = 6
LED_PIN13 = 13
BTN_PIN19 = 19
lasttime = 0
flashtime1 = 1000
flashtime2 = 1300
ledstatus = [GPIO.LOW, GPIO.LOW]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN6, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BTN_PIN19, GPIO.IN, GPIO.PUD_DOWN)


def millis():
    return time.time() * 1000


while True:

    buttonState = GPIO.input(BTN_PIN19)
    currenttime = millis()

    #knop ingedrukt led 1 aan en led 2 uit en omgekeerd voor 1 seconde
    if buttonState == GPIO.HIGH:
        if currenttime - lasttime >= flashtime1:
            lasttime = currenttime
            if ledstatus[0] == GPIO.HIGH and ledstatus[1] == GPIO.LOW:
                ledstatus[0] = GPIO.LOW
                ledstatus[1] = GPIO.HIGH
            else:
                ledstatus[0] = GPIO.HIGH
                ledstatus[1] = GPIO.LOW
            GPIO.output(LED_PIN6, ledstatus[0])
            GPIO.output(LED_PIN13, ledstatus[1])

    #knop niet ingedrukt led 1 aan en led 2 uit voor 1.3 seconde aan en 0.7 seconde uit
    if buttonState == GPIO.LOW:
        if currenttime - lasttime >= flashtime2:
            lasttime = currenttime
            if ledstatus[0] == GPIO.HIGH and ledstatus[1] == GPIO.LOW:
                ledstatus[0] = GPIO.LOW
                ledstatus[1] = GPIO.HIGH
                flashtime2 = 700;
            else:
                ledstatus[0] = GPIO.HIGH
                ledstatus[1] = GPIO.LOW
                flashtime2 = 1300
            GPIO.output(LED_PIN6, ledstatus[0])
            GPIO.output(LED_PIN13, ledstatus[1])

