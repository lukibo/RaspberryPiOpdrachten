#bron powerpoint van Hardware Interfacing periode 6 les 2
import RPi.GPIO as GPIO

LED_PIN6 = 6
LED_PIN13 = 13
BTN_PIN = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN6, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, GPIO.PUD_DOWN)

#als de knop wordt ingedrukt gaat de led aan anders staat deze uit
while True:
    buttonState = GPIO.input(BTN_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN6, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN6, GPIO.LOW)