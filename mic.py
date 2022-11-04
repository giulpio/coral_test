#!/usr/bin/env python3


import math
import shutil

import numpy as np
import sounddevice as sd

block_duration=50

columns = 80
low, high = 100, 2000

device = None

samplerate = sd.query_devices(device, 'input')['default_samplerate']

delta_f = (high - low) / (columns - 1)
fftsize = math.ceil(samplerate / delta_f)
low_bin = math.floor(low / delta_f)

a=0


def callback(indata, frames, time, status):
    if any(indata):
        magnitude = np.abs(np.fft.rfft(indata[:, 0], n=fftsize))
        #print(magnitude)
        #
        # 
        # print(indata)
        #magnitude *= args.gain / fftsize
        media=0
        for x in magnitude:
            media = media+x
        media = media / len(magnitude)
        global max_output
        max_output=max(media, max_output)
        #print("now: " + str(media))
        #print("maz: " + str(max_output))
        a = int(media * 255 / 3)
        a=min(a, 255) 
    else:
        print('no input')



