import board
import digitalio

button = digitalio.DigitalInOut(board.GPIO37)  # pin 36
button.direction = digitalio.Direction.INPUT

value = button.value

try:
    while True:
        if value != button.value:
            print("o")
            value = button.value

finally:
    button.deinit()