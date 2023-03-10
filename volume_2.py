
import os
import signal
import subprocess
import sys
import time
import board
import digitalio
import threading

DEBUG = True

# Set desired minimum and maximum values
min = 0
max = 100

# Set the volume change step size
volume_step_size=1

is_Muted = 0
volume = 0



def debug(str):
  if not DEBUG:
    return
  print(str)



def amixer(cmd):
    p = subprocess.Popen("amixer {}".format(cmd), shell=True, stdout=subprocess.PIPE)
    code = p.wait()
    if code != 0:
      raise VolumeError("Unknown error")
      sys.exit(0)
    
    return p.stdout

def sync(output=None):
    if output is None:
      output = amixer("get 'Master'")
      
    lines = output.readlines()
    if DEBUG:
      strings = [line.decode('utf8') for line in lines]
      debug("OUTPUT:")
      debug("".join(strings))
    last = lines[-1].decode('utf-8')
    
    # The last line of output will have two values in square brackets. The
    # first will be the volume (e.g., "[95%]") and the second will be the
    # mute state ("[off]" or "[on]").
    i1 = last.rindex('[') + 1
    i2 = last.rindex(']')

    global is_Muted
    is_Muted= last[i1:i2]
    print('muted: ',is_Muted)
    
    
    i1 = last.index('[') + 1
    i2 = last.index('%')
    # In between these two will be the percentage value.
    pct = last[i1:i2]
    global volume 
    #print(volume)
    volume = pct
    print('volume: ', pct)


class VolumeError(Exception):
  pass


if __name__ == '__main__':
 
    sync()
    amixer("set 'Master' {}%".format(100))

    #print('volume: ', volume)
    #print('muted: ', is_Muted)

    encoder_clk = 4
    encoder_data = 17
    encoder_button = 27

    

    with digitalio.DigitalInOut(board.GPIO39) as encoder_1, digitalio.DigitalInOut(board.GPIO38) as encoder_2, digitalio.DigitalInOut(board.GPIO37) as encoder_3:
        encoder_1.direction = digitalio.Direction.INPUT
        encoder_2.direction = digitalio.Direction.INPUT
        encoder_3.direction = digitalio.Direction.INPUT
        
        '''
        print("Mute State: " + str(is_Muted))
        print("Volume: " + str(volume))
        print("")'''
        clkLastState = encoder_1.value
        btnLastState = encoder_3.value

        while True:
    #        playsound('/home/mendel/coral_test/static/sounds/startup.wav', block=False)
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
