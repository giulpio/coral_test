import board
import digitalio
import time

import os
clear = lambda: os.system('clear')


def get_foo(someobject, foostring):
    return getattr(someobject,foostring)




while True:
    for i in [12,22]:
        l='D'
        l+=str(i)
        #print(l)
        try:
            button = digitalio.DigitalInOut(get_foo(board, l))
            
            b1=button.value
            time.sleep(0.05)
            final = b1 and button.value

            print(l + ': ' + str(final))  
            #print(button.direction)
            button.deinit()
        except:
                pass
    #print("\n\n")
    #time.sleep(0.4)
    clear()








"""
button = digitalio.DigitalInOut(board.PWM_B)  # pin 36
button.direction = digitalio.Direction.INPUT

value = button.value

try:
    while True:
        if value != button.value:
            time.sleep(0.05)
            if button.value:
                print("acceso")
            else:
                print("spento")
            value = not value

finally:
    button.deinit()
    """