
from i2c import i2c1
import time

import adafruit_mpu6050

mpu = adafruit_mpu6050.MPU6050(i2c1)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--del", type=int, default=1)

    args = parser.parse_args()
    a
    delay = args.del

    while True:
        try:
            print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
            print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
            print("Temperature: %.2f C" % mpu.temperature)
            print("")
        except:
            print("error")

        time.sleep(del)
    
