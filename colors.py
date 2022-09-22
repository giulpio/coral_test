import board
import busio
import time

i2c = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)

for n in range(254):
    try:
        i2c.writeto(0x4, bytes([n,n,n,n]), stop=True)
        time.sleep(0.05)
    except:
        n = n-1
for n in range(254):
    try:
        i2c.writeto(0x4, bytes([n,254-n,254-n,n]), stop=True)
        time.sleep(0.05)
    except:
        n = n-1
for n in range(254):
    try:
        i2c.writeto(0x4, bytes([n,254-n,n,254-n]), stop=True)
        time.sleep(0.05)
    except:
        n = n-1
for n in range(254):
    try:
        i2c.writeto(0x4, bytes([n,n,n,n]), stop=True)
        time.sleep(0.05)
    except:
        n = n-1
