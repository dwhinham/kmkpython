import board
import microcontroller
import storage
import usb_cdc
import supervisor
from digitalio import DigitalInOut, Pull

def check_key_combo():
	row1 = DigitalInOut(board.GP0)
	row1.switch_to_input(pull=Pull.DOWN)

	col1 = DigitalInOut(board.GP3)
	col1.switch_to_output()
	col2 = DigitalInOut(board.GP4)
	col2.switch_to_output()

	# Read two top-left keys from matrix
	col1.value = True
	key1_value = row1.value
	col1.value = False
	col2.value = True
	key2_value = row1.value
	col2.value = False

	row1.deinit()
	col1.deinit()
	col2.deinit()

	# Key 1 and 2 pressed: reboot to bootloader
	if key1_value and key2_value:
		microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
		microcontroller.reset()

	# Key 1 pressed: leave REPL and USB drive enabled
	elif not key1_value:
		storage.disable_usb_drive()
		usb_cdc.disable()

check_key_combo()
supervisor.set_next_stack_limit(4096 + 4096)
