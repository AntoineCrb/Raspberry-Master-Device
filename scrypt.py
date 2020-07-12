import RPi.GPIO as GPIO
from pynput import keyboard

a = 26
b = 13
c = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)

def setNumber(n):
    if (n//4==1):
        n-=4
        GPIO.output(c, GPIO.HIGH)
    else: GPIO.output(c, GPIO.LOW)

    if (n//2==1):
        n-=2
        GPIO.output(b, GPIO.HIGH)
    else: GPIO.output(b, GPIO.LOW)

    if (n==1): GPIO.output(a, GPIO.HIGH)
    else: GPIO.output(a, GPIO.LOW)

def forwardFast(): setNumber(0)
def forward(): setNumber(1)
def backward(): setNumber(2)
def rightSpin(): setNumber(3)
def leftSpin(): setNumber(4)
def stop(): setNumber(7)


def on_press(key):
    if key.char == 'z': 
        print('forward')
        forward()
    elif key.char == 's':             
        print('backward')
        backward()
    elif key.char == 'd': 
        print('rightSpin')
        rightSpin()
    elif key.char == 'q': 
        print('leftSpin')
        leftSpin()
    elif key.char == 'a':
        print('forwardFast')
        forwardFast()

def on_release(key):
    stop()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

GPIO.cleanup()