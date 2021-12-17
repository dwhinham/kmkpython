from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.debug_enabled = False
keyboard.tap_time = 750

keyboard.keymap = [
    [
        KC.F13,     KC.F14,     KC.F15,     KC.F16,
        KC.F17,     KC.F18,     KC.F19,     KC.F20,
        KC.F21,     KC.F22,     KC.F23,     KC.F24,
    ],
]

if __name__ == '__main__':
    keyboard.go()
