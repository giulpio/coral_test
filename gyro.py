
from i2c import i2c1
import time

import adafruit_mpu6050

mpu = adafruit_mpu6050.MPU6050(i2c1)



def delta_acceleration():
    try: old
    except:
        print("first time") 
        old = mpu.acceleration
    print("old: %.3f, %.3f, %.3f" % old)
    print("now: %.3f, %.3f, %.3f" %  mpu.acceleration)
    res = tuple(map(lambda i, j: i - j, mpu.acceleration, old))
    print("res: %.3f, %.3f, %.3f" % res)
    old = mpu.acceleration
    return res

def delta_gyro():
    try: old
    except NameError:
        old = mpu.gyro
    res = tuple(map(lambda i, j: i - j, mpu.gyro, old))
    old = mpu.gyro
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
    
