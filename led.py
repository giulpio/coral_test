from i2c import i2c2
import time

def led(r=0, g=0, b=0):
    try:
        i2c2.writeto(0x4, bytes([r,r,g,b]), stop=True)
    except:
        pass

