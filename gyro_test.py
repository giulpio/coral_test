from gyro import delta_gyro as dg
from led import led
from random import randint
import time

if __name__ == "__main__":
    try:
        while True:
            try:
                delta = dg()
                if delta[0] > 0.2 or delta[1] > 0.2 or delta[2] > 0.2:
                    led(randint(0,255), randint(0,255), randint(0,255))
                    time.sleep(0.2)
                    dg()
                    print("move")
                else:
                    pass
            except:
                print("some errors")

    except KeyboardInterrupt:
        print("end")