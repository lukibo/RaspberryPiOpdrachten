import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#led aan voor 0.1 seconde en uit voor 0.1 seconde
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1/10)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1/10)