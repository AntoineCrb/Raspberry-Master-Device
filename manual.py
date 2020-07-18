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
    elif key.char == 'a':
        print('forwardFast')
        control.forward_fast()

def on_release(key):
    control.stop()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
