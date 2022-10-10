import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GPIO37)  # pin 36
button.direction = digitalio.Direction.INPUT

value = button.value

try:
    while True:
        if value != button.value:
            time.sleep(0.05)
            if value:
                print("acceso")
            else:
                print("spento")
            value = not value

finally:
    button.deinit()