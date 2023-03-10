
import board
import digitalio




def status():
    with digitalio.DigitalInOut(board.GPIO10) as s_pin:
        val=s_pin.value
    return val
