import board
import digitalio
import time

import os
clear = lambda: os.system('clear')


def get_foo(someobject, foostring):
    return getattr(someobject,foostring)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'



if __name__ == "__main__":
    try:
        #while True:
        if True:
            for i in [0,30]:
                l='D'
                l+=str(i)
                #print(l)
                try:
                    button = digitalio.DigitalInOut(get_foo(board, l))
                    
                    b1=button.value
                    time.sleep(0.05)
                    final = b1 and button.value
                    if b1:
                        print(l + ': ' + str(final))  
                    #print(button.direction)
                    button.deinit()
                except:
                        print("FAIL: " + l)
                        pass
            #print("\n\n")
            time.sleep(0.2)
            #clear()

    except KeyboardInterrupt:
        button.deinit()


       








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