import board
import busio
import time
import library.led as led



import os

#import simple sound lib
from playsound import playsound

#play shutdown sound sync

def shutdown():
    led.led(255, 50, 0)
    playsound('/home/mendel/coral_test/static/sounds/beep-01a.mp3', block=True)
    print("power cable unplugged --> closing program and shutdown system")
    led.led(0,0,0)
    os.system("sudo shutdown")
    
if __name__ == "__main__":
    shutdown()
