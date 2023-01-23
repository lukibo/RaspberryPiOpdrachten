#bron powerpoint van Hardware Interfacing periode 6 les 2
import RPi.GPIO as GPIO
import time

LED_PIN6 = 6
LED_PIN13 = 13
BTN_PIN = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN6, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, GPIO.PUD_DOWN)

#als de knop wordt ingedrukt gaat de eerste led voor 1.3s aan en 0.7s uit en de staat de tweede led uit,
#als de knop niet ingedrukt is staat de eerste uit en de tweede led aan
while True:
    buttonState = GPIO.input(BTN_PIN)

    if buttonState == GPIO.HIGH:
        GPIO.output(LED_PIN13, GPIO.LOW)
        GPIO.output(LED_PIN6, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN6, GPIO.LOW)
        time.sleep(0.7)
    else:
        GPIO.output(LED_PIN6, GPIO.LOW)
        GPIO.output(LED_PIN13, GPIO.HIGH)