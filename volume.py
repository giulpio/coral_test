
from playsound import playsound
from time import sleep
import board
import digitalio
import os
import alsaaudio

m = alsaaudio.Mixer()

print(dir(m))
# Change the following pins based on your application or HAT in use
encoder_clk = 4
encoder_data = 17
encoder_button = 27


encoder_1 = digitalio.DigitalInOut(board.GPIO39)  # pin 40
encoder_1.direction = digitalio.Direction.INPUT

encoder_2 = digitalio.DigitalInOut(board.GPIO38)  # pin 40
encoder_2.direction = digitalio.Direction.INPUT

encoder_3 = digitalio.DigitalInOut(board.GPIO37)  # pin 40
encoder_3.direction = digitalio.Direction.INPUT




#m = alsaaudio.Mixer()

# Set desired minimum and maximum values
min = 0
max = 100

# Set the volume change step size
volume_step_size=5

is_Muted = 0
volume = 0

volume = m.getvolume()
volume = int(volume[0])

if is_Muted == 0:
    is_Muted=False
else:
    is_Muted=True
print("Mute State: " + str(is_Muted))
print("Volume: " + str(volume))
print("")
clkLastState = encoder_1.value
btnLastState = encoder_3.value



try:
    while True:
#        playsound('/home/mendel/coral_test/static/sounds/startup.wav', block=False)
        btnPushed = encoder_3.value
        volume = m.getvolume()
        volume = int(volume[0])
        if ((not btnLastState) and btnPushed):
            if is_Muted:
                is_Muted = False
                #m.setmute(0)
                print("Mute State: " + str(is_Muted))
                print("Volume: " + str(int(volume)))
                print("")
            else:
                is_Muted = True
                #m.setmute(1)from time import sleep

                print("Mute State: " + str(is_Muted))
                print("Volume: " + str(int(volume)))
                print("")
            sleep(0.05)
        else:
            clkState = encoder_1.value
            dtState = encoder_2.value
            if clkState != clkLastState:
                if dtState != clkState:
                    vol = m.getvolume()
                    vol = int(vol[0])
                    newVol = vol - volume_step_size
                    if newVol > max:
                        newVol = max
                else:
                    vol = m.getvolume()
                    vol = int(vol[0])
                    newVol = vol + volume_step_size
                    if newVol < min:
                        newVol = min
                try:
                    m.setvolume(newVol)
                except:
                    pass
                if clkState == 1:
                    print("Mute State: " + str(is_Muted))
                    print("Volume: " + str(int(volume)))
                    print("")
            clkLastState = clkState
        btnLastState = btnPushed
finally:
    encoder_1.deinit()
    encoder_2.deinit()
    encoder_3.deinit()





