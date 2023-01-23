#Bron powerpoint van brightspace, https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/28BYJ.md en Elske Asselbergs
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

btn_PIN1 = 20
btn_PIN2 = 21
gpioPins = [6,13,19,26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_PIN1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(btn_PIN2, GPIO.IN, GPIO.PUD_DOWN)

DCMotor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")

fast = (5 / 4096)
slow = (12 / 4096)

#functie voor het indrukken van een specifieke knop
try:
    while True:
        buttonStateA = GPIO.input(btn_PIN1)
        buttonStateB = GPIO.input(btn_PIN2)

        #snelle draai van 5 seconden
        if buttonStateA == GPIO.HIGH:
            DCMotor.motor_run(gpioPins, fast, 512, False, True, "half", 0)
        #langzame draai van 12 seconden
        if buttonStateB == GPIO.HIGH:
            DCMotor.motor_run(gpioPins, slow, 512, True, True, "half", 0)

finally:
    GPIO.cleanup()