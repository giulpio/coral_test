from library.gyro import delta_gyro as dg
from library.led import led
from random import randint
import time

if __name__ == "__main__":
    try:
        while True:
            try:
                delta = dg()
                if delta[0] > 0.05 or delta[1] > 0.05 or delta[2] > 0.05:
                    led(randint(0,255), randint(0,255), randint(0,255))
                    #time.sleep(0.2)
                    dg()
                    print("move")
                else:
                    pass
            except:
                print("some errors")
                raise TypeError

    finally:
        print("end")