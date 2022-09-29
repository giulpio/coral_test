
import time
import board
import busio
import adafruit_mpu6050

i2c1 = busio.I2C(board.I2C1_SCL, board.I2C1_SDA)
i2c2 = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)

mpu = adafruit_mpu6050.MPU6050(i2c1)

i2c2.writeto(0x4, bytes([0,255,0,0]), stop=True)

while True:
    
    
    """
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
    """