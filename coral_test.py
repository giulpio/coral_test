import startup
import shutdown
import i2c
#import gyro
from gyro import move
from led import led
from buttons import *
from random import randint

import time

startup.startup()
time.sleep(1)

while True:
    if read(switch):
        led(255,255,255)
    elif read(button1):
        led(0,255,0)
        pass
    elif read(button2):
        led(0,0,255)
        pass
    elif move(0.08):
        led(randint(0,255), randint(0,255), randint(0,255))
        pass
    else:
        pass



"""

state = 0
maxstate = 2



try:
    while True:
        if read(switch):
            print("read_switch")
            #time.sleep(1)
            #state+=1
            #if state > maxstate:
            #    state = 0
            led(0,0,255)
            print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (gyro.mpu.acceleration))
        if state == 0:
            if read(button1):
                led(255,0,0)
            elif read(button2):
                led(0,255,0)
            else:
                led(255,255,255)
        elif state == 1:
            led(0,0,255)
        else:
            led(0,0,0)
        
        if gyro.mpu.acceleration[1] > 2 or gyro.mpu.acceleration[1] < -1:
            led(255,255,0)
        #time.sleep(0.2)


except KeyboardInterrupt:
    deinit()
    print("error")
#shutdown.shutdown()"""