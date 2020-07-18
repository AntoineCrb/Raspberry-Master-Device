import RPi.GPIO as GPIO

# rpi pins - GPIO BCM mode
a = 26
b = 13
c = 6

class Control:
    current=0
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(a, GPIO.OUT)
        GPIO.setup(b, GPIO.OUT)
        GPIO.setup(c, GPIO.OUT)

        self.set_number(7) # stop

    def get_current_state(self): return self.current
    def set_number(self, n): # convert decimal number to binary information with pins
        self.current=n
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

    def forward_fast(self): self.set_number(0)
    def forward(self): self.set_number(1)
    def backward(self): self.set_number(2)
    def right_spin(self): self.set_number(3)
    def left_spin(self): self.set_number(4)
    def stop(self): self.set_number(7)
