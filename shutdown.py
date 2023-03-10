import board
import busio
import time

import os

#import simple sound lib
from playsound import playsound

#play shutdown sound sync

def shutdown():
    playsound('/home/mendel/coral_test/beep-01a.mp3', block=True)
    print("power cable unplugged --> closing program and shutdown system")
    os.system("sudo shutdown")
    
if __name__ == "__main__":
	shutdown()
