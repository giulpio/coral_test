from i2c import i2c2
import time

rg,gg,bg = 0,0,0

#send led color
def send(r=0, g=0, b=0):
    success=False
    global rg, gg, bg
    rg, gg, bg = r,g,b
    count = 0
    while not success and count < 25:
        try:
            i2c2.writeto(0x4, bytes([b,r,g,b]), stop=True)
            success = True
        except:
            count = count + 1
            print("can't send to led")
            pass


#use this to set led single color
def led(r,g,b):
    while not i2c2.try_lock():
        pass      
    try:
        send(r,g,b)
    finally:
        global rg, gg, bg
        rg, gg, bg = r,g,b
        i2c2.unlock()
 
def led_low():
    global rg, gg, bg
    rg = rg-1 if rg>0 else 0 
    gg = gg-1 if gg>0 else 0 
    bg = bg-1 if bg>0 else 0 
    led(rg, gg, bg)

#function to fade led colors
def led_fade(t):
    while not i2c2.try_lock():
        pass     
    try:
        #r=0--> 255
        #g=255-->0
        #b = 125 --> 0 --> 125
        for i in range(255):
            b=i-125
            if b<0:
                b=-b
            send(i, 255-i, b)
            time.sleep(t)
        #r=255--> 0
        #g=0-->255
        #b = 125 --> 255 --> 125
        for i in range(255):
            b=i+125
            if b>255:
                b=255 + 125 -b
            send(255-i, i, b)
            time.sleep(t)
    finally:
        global rg, gg, bg
        rg, gg, bg = r,g,b
        i2c2.unlock()



if __name__ == "__main__":
    try:
        while(True):
            try:
                led_fade(200)
            except:
                pass
    except KeyboardInterrupt:
        print("Ciao")
