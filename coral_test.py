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

from volume_2 import *

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
            

            encoder_clk = 4
            encoder_data = 17
            encoder_button = 27

            clkLastState = encoder_1.value
            btnLastState = encoder_3.value

            sync()

            
            with digitalio.DigitalInOut(board.GPIO39) as encoder_1, digitalio.DigitalInOut(board.GPIO38) as encoder_2, digitalio.DigitalInOut(board.GPIO37) as encoder_3:
                encoder_1.direction = digitalio.Direction.INPUT
                encoder_2.direction = digitalio.Direction.INPUT
                encoder_3.direction = digitalio.Direction.INPUT


                clkLastState = encoder_1.value
                btnLastState = encoder_3.value
            
            
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

                    

                    btnPushed = encoder_3.value
                    if ((not btnLastState) and btnPushed):
                        print('press')
                        time.sleep(0.2)
                        if is_Muted:
                            is_Muted = False
                            #amixer("set 'Master' on")
                            '''print("Mute State: " + str(is_Muted))
                            print("Volume: " + str(int(volume)))
                            print("")'''
                            try:
                                led(255,0,0)
                            except:
                                pass
                        else:
                            is_Muted = True
                            #m.setmute(1)from time import sleep
                            #amixer("set 'Master' off")
                            '''print("Mute State: " + str(is_Muted))
                            print("Volume: " + str(int(volume)))
                            print("")'''
                        #sync()
                        
                    else:
                        clkState = encoder_1.value
                        dtState = encoder_2.value
                        if clkState != clkLastState:
                            #print('clkState: ',clkState, ' dtState: ', dtState )
                            #time.sleep(0.2)     
                            if dtState == clkState:
                                #vol = m.getvolume()
                                #vol = int(vol[0])
                                vol = int(volume)
                                newVol = vol - volume_step_size
                                
                                
                            else:
                                #vol = m.getvolume()
                                #vol = int(vol[0])
                                vol = int(volume)
                                newVol = vol + volume_step_size
                                
                            
                            if newVol > max:
                                    newVol = max
                            
                            if newVol < min:
                                    newVol = min
                            try:
                                #amixer("set 'Master' {}%".format(newVol))
                                t1 = threading.Thread(target=amixer, args = ['set Master {}%'.format(newVol)])
                                t1.daemon= True
                                t1.start()
                                if(volume != newVol):
                                    print(newVol)
                                volume = newVol
                                try:
                                    led(0,0,int(255*(volume/100)))
                                except:
                                    pass
                            except:
                                pass
                            '''
                            if clkState == 1:
                                print("Mute State: " + str(is_Muted))
                                print("Volume: " + str(int(volume)))
                                print("")'''
                            #sync()
                            
                        clkLastState = clkState
                    btnLastState = btnPushed

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