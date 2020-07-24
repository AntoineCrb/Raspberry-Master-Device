from pynput import keyboard
from communication.control import Control

control = Control()

def on_press(key):
    if key.char == 'z': 
        print('forward')
        control.forward()
    elif key.char == 's':             
        print('backward')
        control.backward()
    elif key.char == 'd': 
        print('rightSpin')
        control.right_spin()
    elif key.char == 'q': 
        print('leftSpin')
        control.left_spin()

    elif key.char == 'r': 
        print('left1')
        control.left1()
    elif key.char == 't': 
        print('left2')
        control.left2()
    elif key.char == 'y': 
        print('left3')
        control.left3()
    elif key.char == 'u': 
        print('left4')
        control.left4()

    elif key.char == 'f': 
        print('right1')
        control.right1()
    elif key.char == 'g': 
        print('right2')
        control.right2()
    elif key.char == 'h': 
        print('right3')
        control.right3()
    elif key.char == 'j': 
        print('right4')
        control.right4()
        
def on_release(key):
    control.stop()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
