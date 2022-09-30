from i2c import i2c2
import time

def led(r=0, g=0, b=0):
    success=False
    while not success:
        try:
            i2c2.writeto(0x4, bytes([r,r,g,b]), stop=True)
            success = True
        except:
            print("suca")
            pass


def led_fade(t):
    for i in range(255):
        b=i-125
        if b<0:
            b=-b
        led(i, 255-i, b)
        time.sleep(t)
