import board
import busio

i2c = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)

for n in range(255):
    try:
        i2c.writeto(0x4, bytes([n,n,n,n]), stop=True)
    except:
        n = n-1
