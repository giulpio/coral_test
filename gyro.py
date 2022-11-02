
from i2c import i2c1
import time
import adafruit_mpu6050



mpu = adafruit_mpu6050.MPU6050(i2c1)

old_g= (0,0,0)
old_a=(0,0,0)

max_g =(0,0,0)
max_a=(0,0,0)




#compute delta between instant acceleration and previous acceleration
#mm/s
def delta_acceleration():
    global old_a
    #print("old: %.3f, %.3f, %.3f" %  old_a)
    #print("now: %.3f, %.3f, %.3f" %  mpu.acceleration)
    res = tuple(map(lambda i, j: i - j, mpu.acceleration, old_a))
    #print("res: %.3f, %.3f, %.3f" % res)
    old_a = mpu.acceleration
    return res

#rad/s
def delta_gyro():
    global old_g
    res = tuple(map(lambda i, j: i - j, mpu.gyro, old_g))
    old_g = mpu.gyro
    return res



#detect movements in range 
def move(trigger=0.05):
    try:
        delta = delta_gyro()
        if delta[0] > trigger or delta[1] > trigger or delta[2] > trigger:
            return True
        else:
            return False
    except:
        return True






#use this for testing

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--delay", type=int, default=1)

    args = parser.parse_args()
    delay = args.delay

    while True:
        try:
            delta_a = delta_acceleration()
            delta_g = delta_gyro()
            print("Delta Acceleration: %.3f, %.3f, %.3f" %  delta_a)
            print("        Delta Gyro: %.3f, %.3f, %.3f" %  delta_g)
            print("")
            max_a = (max(delta_a[0], max_a[0]),  max(delta_a[1], max_a[1]), max(delta_a[2], max_a[2]))
            print("  MAX Acceleration: %.3f, %.3f, %.3f" % max_a)
            max_g = (max(delta_g[0], max_g[0]), max(delta_g[1], max_g[1]), max(delta_g[2], max_g[2]))
            print("          MAX Gyro: %.3f, %.3f, %.3f" % max_g)
            #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
            #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
            #print("Temperature: %.2f C" % mpu.temperature)
            #print("")
        except:
            print("error")

        time.sleep(delay)
    
