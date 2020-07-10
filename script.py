import RPi.GPIO as GPIO

a = 25
b = 24
c = 23
d = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)

def setNumber(n):
    if (n%8==1):
        n-=8
        GPIO.output(d, GPIO.HIGH)
    else: GPIO.output(d, GPIO.LOW)

    if (n%4==1):
        n-=4
        GPIO.output(c, GPIO.HIGH)
    else: GPIO.output(c, GPIO.LOW)

    if (n%2==1):
        n-=2
        GPIO.output(b, GPIO.HIGH)
    else: GPIO.output(b, GPIO.LOW)

    if (n==1): GPIO.output(a, GPIO.HIGH)
    else: GPIO.output(a, GPIO.LOW)

def stop(): setNumber(0)
def forward(): setNumber(1)
def backward(): setNumber(2)
def rightSpin(): setNumber(3)
def leftSpin(): setNumber(4)

while True:
    inkey = input()
    if inkey == 'a': 
        print('stop')
        stop()
    if inkey == 'z': 
        print('forward')
        forward()
    if inkey == 's':
        print('backward')
        backward()
    if inkey == 'd': 
        print('rspin')
        rightSpin()
    if inkey == 'q': 
        print('lspin')
        leftSpin()
    if inkey == 'e': 
        print('end')
        break