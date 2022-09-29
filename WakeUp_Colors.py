import board
import busio
import time

i2c = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)
for i in range(3):	
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

