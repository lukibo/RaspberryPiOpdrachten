#bron Jeremy
import RPi.GPIO as GPIO

knopPin = 6
leds = [26, 19]
Ardpins = [3, 4]

GPIO.setmode(GPIO.BCM)

GPIO.setup(knopPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leds[0], GPIO.OUT)
GPIO.setup(leds[1], GPIO.OUT)
GPIO.setup(Ardpins[0], GPIO.IN)
GPIO.setup(Ardpins[1], GPIO.OUT)

#functie voor het regelen van de pinnen
while True:
    GPIO.output(Ardpins[1], GPIO.input(knopPin))

    if GPIO.input(Ardpins[0]) == GPIO.HIGH:
        GPIO.output(leds[0], GPIO.HIGH)
        GPIO.output(leds[1], GPIO.LOW)
    else:
        GPIO.output(leds[1], GPIO.HIGH)
        GPIO.output(leds[0], GPIO.LOW)