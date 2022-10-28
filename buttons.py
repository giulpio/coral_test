#switch gpio45
#neo gpio13
#button1 uart1tx
#button2 uart1rx

import board
import digitalio
import time

button1 = digitalio.DigitalInOut(board.D12)
button2 = digitalio.DigitalInOut(board.D22)
switch = digitalio.DigitalInOut(board.D19)
neo = digitalio.DigitalInOut(board.D16)




"""
from symbol import classdef


class button:
    def __init__(self, pin):
        self.btn = digitalio.DigitalInOut(pin)
        self.value = self.btn.value
   
    


button1 = button(board.PWM_A)
button2 = button(board.PWM_B)
switch = button(board.GPIO37)
neo = button(board.GPIO13)


#button1 = digitalio.DigitalInOut(board.UART1TX)
#button2 = digitalio.DigitalInOut(board.UART1RX)
#switch = digitalio.DigitalInOut(board.GPIO45)
#neo = digitalio.DigitalInOut(board.GPIO13)

"""

