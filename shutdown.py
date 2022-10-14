import board
import busio
import time


#import simple sound lib
from playsound import playsound

#initilaize i2c
i2c = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)

#play startup sound async
playsound('/home/mendel/coral_test/beep-01a.mp3', block=True)
