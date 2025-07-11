# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

from kmk.scanners import DiodeOrientation

COL_PINS = (board.GPIO0, board.GPIO3, board.GPIO4)
ROW_PINS = (board.GPIO1, board.GPIO2)

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

keyboard.matrix = MatrixScanner(
    row_pins=ROW_PINS,
    col_pins=COL_PINS,
    diode_orientation=MatrixScanner.DIODE_COL2ROW,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.1, KC.2, KC.3, KC.4, KC.5, KC.6]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()