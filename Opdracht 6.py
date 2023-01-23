#bron powerpoint van Hardware Interfacing periode 6 les 2, Eloi Bastien
import RPi.GPIO as GPIO
import time

btn13 = 13
btn19 = 19
SERVO_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn13, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(btn19, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def millis():
    return time.time() * 1000


curTime = millis()
SerLastTime = millis()
wait = millis()

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)


Normal = False
Fast = False

while True:

    curTime = millis()
    buttonStateA = GPIO.input(btn13)
    buttonStateB = GPIO.input(btn19)

    global timing

    if buttonStateA == GPIO.HIGH:
        if not Normal:
            Normal = True
            SerLastTime = millis()
            timing = 1000

    if buttonStateB == GPIO.HIGH:
        if not Normal:
            Normal = True
            SerLastTime = millis()
            timing = 500

    if Normal:
        if not Fast:
            if (curTime - SerLastTime) >= timing:
                servoLastTime = millis()
                SetAngle(120)
                Fast = True
        if Fast:
            if (curTime - SerLastTime) >= timing:
                SetAngle(0)
                Fast = False
                Normal = False

