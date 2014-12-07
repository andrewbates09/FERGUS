import RPi.GPIO as GPIO
import time

''' VARIABLES '''

def turnOn(pin):
    print("set high: ", pin)
    GPIO.output(pin,GPIO.HIGH)
    return

def turnOff(pin):
    print("set low: ", pin)
    GPIO.output(pin, GPIO.LOW)
    return

def cycleLights(a, b, c):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)

    for i in range(0,3):
        print("start loop")
        turnOn(a)
        time.sleep(.8)
        turnOff(a)
        turnOn(b)
        time.sleep(.8)
        turnOff(b)
        turnOn(c)
        time.sleep(.8)
        turnOff(c)
    return

cycleLights(11, 19, 29)
GPIO.cleanup()
