import RPi.GPIO as GPIO
import time

LED_PIN16 = 16
LED_PIN21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN21, GPIO.OUT)
#eerste led 1.3s aan en 0.7s uit en dan tweede led 0.8s aan en 1.7s uit
while True:
    GPIO.output(LED_PIN16, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_PIN16, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(LED_PIN21, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_PIN21, GPIO.LOW)
    time.sleep(1.7)
