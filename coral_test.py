from startup import startup
from shutdown import shutdown
import library.i2c as i2c 
#import gyro
from library.gyro import move
from library.led import led, led_low
from library.buttons import *
from random import randint

from library.mic import *

from library.status import status

import time
from timeit import default_timer as timer

last_act = timer()


printmic = False


def led_mic(indata, frames, time, status):
    if any(indata):
        magnitude = np.abs(np.fft.rfft(indata[:, 0], n=fftsize))
        media=0
        for x in magnitude:
            media = media+x
        media = media / len(magnitude)
        bright = int(media * 255 / 2.8)
        bright=min(bright, 255) 
        #print(bright)
        global printmic
        if printmic:
            led(bright,bright,bright)
            printmic=False
        
    else:
        print('no input')


if __name__ == '__main__':
    

    try:
        startup()
        time.sleep(1)
        with sd.InputStream(device=device, channels=1, callback=led_mic,
                                blocksize=int(samplerate * block_duration / 1000),
                                samplerate=16000):#samplerate):
            while status():
            
                if read(switch):    
                    printmic = True
                    #print(a)
                    #led(a,a,a)
                    last_act = timer()
                elif read(button):
                    led(255,0,0)
                    last_act=timer()
                    pass
                elif move(0.08):
                    led(randint(0,255), randint(0,255), randint(0,255))
                    last_act=timer()
                    pass
                else:
                    if timer() - last_act > 0.01:
                        #print("low")
                        last_act = timer()
                        led_low(5)
                    pass
        shutdown()
        
    except KeyboardInterrupt:
        print('Interrupted by user')
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))

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