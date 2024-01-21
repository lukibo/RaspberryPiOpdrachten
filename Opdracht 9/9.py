#bron Elske

import RPi.GPIO as GPIO
import time

ledPinnen = [26, 19, 13, 6]
arduinoPinnen = [11, 9, 10, 22]
knipperTijden = [300, 500, 800, 1000]
vorigeTijden = [0, 0, 0, 0]
vorigeLedInput = -1
ledStatussen = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
knipperSelectie = [0, 0, 0, 0]
vorigeLed = [0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

# GPIO-uitgangsinstellingen
for i in range(4):
    GPIO.setup(ledPinnen[i], GPIO.OUT)

# GPIO-ingangsinstellingen met pull-up weerstand
for i in range(4):
    GPIO.setup(arduinoPinnen[i], GPIO.IN, GPIO.PUD_UP)

def millis():
    return time.time() * 1000

#functie voor het controleren van de led
def controleerLed(led, tijd):
    if vorigeLed[led] == 0:
        s = 0
        for i in vorigeLed:
            if i == 2:
                ledStatussen[s] = GPIO.LOW
                vorigeLed[s] = 0
                GPIO.output(ledPinnen[s], GPIO.LOW)
            if i == 1:
                vorigeLed[s] = 2
            s += 1
        ledStatussen[led] = GPIO.HIGH
        vorigeLed[led] = 1
        GPIO.output(ledPinnen[led], GPIO.HIGH)

    knipperSelectie[led] = knipperTijden[tijd]
    knipperLed(led)

#functie voor het knipperen van de led
def knipperLed(led):
    huidigeTijd = millis()
    if huidigeTijd - vorigeTijden[led] >= knipperSelectie[led] and vorigeLed[led] >= 1:
        vorigeTijden[led] = huidigeTijd
        if ledStatussen[led] == GPIO.LOW:
            ledStatussen[led] = GPIO.HIGH
        else:
            ledStatussen[led] = GPIO.LOW
        GPIO.output(ledPinnen[led], ledStatussen[led])

#functie die de input regelt
def ledInput(i):
    global vorigeLedInput
    pinStatus = GPIO.input(arduinoPinnen[i])
    if pinStatus == GPIO.HIGH:
        if vorigeLedInput > -1:
            controleerLed(vorigeLedInput, i)
            vorigeLedInput = -1
        else:
            vorigeLedInput = i

controleerLed(0, 0)
controleerLed(1, 0)

#loop voor het doorlopen van alle leds
while True:
    for i in range(4):
        knipperLed(i)
        ledInput(i)
    time.sleep(0.1)
