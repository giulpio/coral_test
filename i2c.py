import board
import busio

i2c1 = busio.I2C(board.I2C1_SCL, board.I2C1_SDA)
i2c2 = busio.I2C(board.I2C2_SCL, board.I2C2_SDA)
