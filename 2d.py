import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#snelheid waarbij het lijkt alsof de led continu brand
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1/100)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1/100)