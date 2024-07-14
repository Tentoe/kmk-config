# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default


import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split, SplitSide
from kmk.modules.combos import Combos, Chord

keyboard = KMKKeyboard()

combos = Combos()

keyboard.modules = [
    Layers(combo_layers={(1, 2): 3, (4, 5): 6}),
    combos,
    Split(
        # TODO cange depending on side
        split_side=SplitSide.LEFT,
        # TODO splt_target is the side which will be connected to USB
        split_target_left=True,
        # TODO depending on the board you are using you need to set use_pio=True
        use_pio=True,
        split_flip=True,
        data_pin=board.RX,
        uart_flip=True,
    ),
    HoldTap(),
    MouseKeys(),
]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO


# Mod-taps
A_SUP = KC.HT(KC.A, KC.LGUI)  # pyright: ignore
S_ALT = KC.HT(KC.S, KC.LALT)  # pyright: ignore
D_CTL = KC.HT(KC.D, KC.LCTRL)  # pyright: ignore
F_SFT = KC.HT(KC.F, KC.LSFT)  # pyright: ignore

QUOT_SUP = KC.HT(KC.QUOT, KC.LGUI)  # pyright: ignore
L_ALT = KC.HT(KC.L, KC.LALT)  # pyright: ignore
K_CTL = KC.HT(KC.K, KC.LCTRL)  # pyright: ignore
J_SFT = KC.HT(KC.J, KC.LSFT)  # pyright: ignore


# Layer tap for other home row keys
# DEL_L1 = KC.LT(1, KC.DEL)
BSPC_L2 = KC.LT(2, KC.BSPC)  # pyright: ignore
ENT_L3 = KC.LT(3, KC.ENT)  # pyright: ignore

TAB_L4 = KC.LT(4, KC.TAB)  # pyright: ignore
SPC_L5 = KC.LT(5, KC.SPACE)  # pyright: ignore
# ESC_L6 = KC.LT(6, KC.ESC)

combos.combos = [
    Chord((15, 16), KC.LT(1, KC.DEL), match_coord=True),  # pyright: ignore
    Chord((30, 32), KC.LT(6, KC.ESC), match_coord=True),  # pyright: ignore
]

# fmt: off
      # _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
keyboard.keymap = [
    [  # QWERTY
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        A_SUP,   S_ALT,   D_CTL,   F_SFT,   KC.G,    KC.H,    J_SFT,   K_CTL,   L_ALT,   QUOT_SUP,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
                                   BSPC_L2, ENT_L3,  TAB_L4,  SPC_L5,
    ],
    [  # Funcion
        _______, _______, _______, _______, _______, KC.PSCR,   KC.F7,   KC.F8,   KC.F9,  KC.F12,
        _______, _______, _______, _______, _______, KC.SLCK,   KC.F4,   KC.F5,   KC.F6,  KC.F11,
        _______, _______, _______, _______, _______, KC.PAUS,   KC.F1,   KC.F2,   KC.F3,  KC.F10,
                                   _______, _______, _______, _______,
    ],
    [  # Numbers
        _______, _______, _______, _______, _______, KC.LBRC,    KC.7,    KC.8,    KC.9, KC.RBRC,
        _______, _______, _______, _______, _______,  KC.EQL,    KC.4,    KC.5,    KC.6, KC.SCLN,
        _______, _______, _______, _______, _______, KC.BSLS,    KC.1,    KC.2,    KC.3,  KC.GRV,
                                   _______, _______, _______, _______,
    ],
    [  # RIGHT SYMBOLS
        _______, _______, _______, _______, _______, _______, KC.UNDS, KC.PIPE, KC.QUOT, _______,
        KC.CIRC, KC.ASTR, KC.AMPR, _______, _______, KC.HASH, KC.TILD, KC.SLSH, KC.DQUO,  KC.DLR,
        _______, _______, _______, _______, _______, _______, KC.MINS, KC.BSLS,  KC.GRV, _______,
                                   _______, _______, _______, _______,
    ],
    [  # LEFT SYMBOLS
        _______, KC.COLN, KC.LABK, KC.RABK, KC.SCLN, _______, _______, _______, _______, _______,
        KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN,   KC.AT, _______, _______,  KC.EQL, KC.PLUS, KC.PERC,
        _______, KC.EXLM, KC.LBRC, KC.RBRC, _______, _______, _______, _______, _______, _______,
                                   _______, _______, _______, _______,
    ],
    [  # 5 FUNCTION
        _______, _______, _______, _______, _______, _______, KC.F7, KC.F8, KC.F9, KC.F10,
        _______, _______, _______, _______, _______, _______, KC.F4, KC.F5, KC.F6, KC.F11,
        _______, _______, _______, _______, _______, _______, KC.F1, KC.F2, KC.F3, KC.F12,
                                   _______, _______, _______, _______,
    ],
    [  # 6 NUMBERS
        KC.SLSH,   KC.N7,   KC.N8,   KC.N9, KC.PLUS, _______, _______, _______, _______, _______,
          KC.N0,   KC.N1,   KC.N2,   KC.N3, KC.MINS, _______, _______, _______, _______, _______,
        KC.ASTR,   KC.N4,   KC.N5,   KC.N6,  KC.EQL, _______, _______, _______, _______, _______,
                                   _______, _______, _______, _______,
    ],
    [  # 7 ALWAYS AVAILABLE
        _______, _______, KC.COLN,  KC.ESC, _______, _______, _______, _______, _______,  KC.DEL,
        _______, KC.PERC, KC.SLSH,  KC.ENT, _______, KC.A, KC.LGUI, _______, _______, _______,
        _______, _______, _______, KC.PERC, _______, KC.B, KC.RALT, KC.RCTL, _______, KC.RESET,
                                   _______,  KC.TAB, _______, _______,
    ],
]
# fmt:on

if __name__ == "__main__":
    keyboard.go()
