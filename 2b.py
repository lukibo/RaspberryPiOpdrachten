import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#led aan voor 1 seconde en uit voor 2 seconden
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)