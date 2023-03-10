
import board
import digitalio




def status():
    with digitalio.DigitalInOut(board.GPIO10) as s_pin:
        val=s_pin.value
        s_pin.deinit()
    return val
