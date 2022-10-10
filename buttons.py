#switch gpio45
#neo gpio13
#button1 uart1tx
#button2 uart1rx

from msilib.schema import Class
import board
import digitalio
import time

from symbol import classdef


class button:
    def __init__(self, pin):
        self.btn = digitalio.DigitalInOut(pin)
        self.value = self.btn.value
   
    


button1 = button(board.UART1TX)
button2 = button(board.UART1RX)
switch = button(board.GPIO45)
neo = button(board.GPIO13)


#button1 = digitalio.DigitalInOut(board.UART1TX)
#button2 = digitalio.DigitalInOut(board.UART1RX)
#switch = digitalio.DigitalInOut(board.GPIO45)
#neo = digitalio.DigitalInOut(board.GPIO13)



