#!/usr/bin/python3
import sys
sys.path.append('/usr/local/lib/python3.7/dist-packages')


#import coral I/O
import board
import busio
import time
import library.led as led


#import simple sound lib
from playsound import playsound

#initilaize i2c
i2c = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)

#play startup sound async
#playsound('/home/mendel/coral_test/Windows XP Startup.mp3', block=False)
playsound('.static/sounds/startup.wav', block=False)
""""
def startup():
	#led fade
	for i in range(2):      
		for n in range(50):
			try:
				i2c.writeto(0x4, bytes([n,n,n,n]), stop=True)
				time.sleep(0.01)
			except:
				n = n-1
			#print("error")

		time.sleep(0.3)

		for n in range(50):
			try:
				i2c.writeto(0x4, bytes([49-n,49-n,49-n,49-n]), stop=False)
				time.sleep(0.01+i/100)
			except:
				n = n-1
				#print("error")

if __name__ == "__main__":
	print("starting...")
	startup()
	print("ok")
"""

def startup():
	#led fade
	for i in range(2):      
		for n in range(50):
			try:
				led.led(n,n,n)
				time.sleep(0.01)
			except:
				n = n-1
			#print("error")

		time.sleep(0.3)

		for n in range(50):
			try:
				l=50-n
				led.led(l,l,l)
				time.sleep(0.01+i/100)
			except:
				n = n-1
				#print("error")


if __name__ == "__main__":
	print("starting...")
	startup()
	print("ok")