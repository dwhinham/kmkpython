import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
    )
    col_pins = (
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
    )
    diode_orientation = DiodeOrientation.COLUMNS
