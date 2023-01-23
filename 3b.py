import RPi.GPIO as GPIO
import time

LED_PIN16 = 16
LED_PIN21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN21, GPIO.OUT)
#1 led aan en 1 led uit en omgekeerd met intervallen van 1 seconde
while True:
    GPIO.output(LED_PIN16, GPIO.HIGH)
    GPIO.output(LED_PIN21, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_PIN21, GPIO.HIGH)
    GPIO.output(LED_PIN16, GPIO.LOW)
    time.sleep(1)