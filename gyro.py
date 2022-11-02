
from i2c import i2c1
import time

import adafruit_mpu6050

mpu = adafruit_mpu6050.MPU6050(i2c1)

old_g= (0,0,0)
old_a=(0,0,0)


def delta_acceleration():
    global old_a
    print("old: %.3f, %.3f, %.3f" %  old_a)
    print("now: %.3f, %.3f, %.3f" %  mpu.acceleration)
    res = tuple(map(lambda i, j: i - j, mpu.acceleration, old_a))
    print("res: %.3f, %.3f, %.3f" % res)
    old_A = mpu.acceleration
    return res

def delta_gyro():
    global old_g
    res = tuple(map(lambda i, j: i - j, mpu.gyro, old_g))
    old_g = mpu.gyro
    return res


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--delay", type=int, default=1)

    args = parser.parse_args()
    delay = args.delay

    while True:
        try:
            print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
            print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
            print("Temperature: %.2f C" % mpu.temperature)
            print("")
        except:
            print("error")

        time.sleep(delay)
    
