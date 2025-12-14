import board
import adafruit_neopixel
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

PIXEL_PIN = board.GP11
NUM_LEDS = 9
BRIGHTNESS = 0.25

pixels = adafruit_neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_LEDS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=adafruit_neopixel.GRB
)

def clear_leds():
    for i in range(NUM_LEDS):
        pixels[i] = (0, 0, 0)
    pixels.show()

clear_leds()

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8,
]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=True)

LED_MAP = {
    0: [0],
    1: [1],
    2: [2, 3],
    3: [4],
    4: [5, 6],
    5: [7],
    6: [8],
}

LED_COLORS = {
    'single': (255, 120, 0),
    'double': (255, 180, 0),
    'stealth': (0, 0, 0)
}

class LEDTimerModule:
    def __init__(self, timeout=2.0):
        self.timeout = timeout
        self.timer = None
        self.current_key = None
        self.last_pressed = set()
    
    def during_bootup(self, keyboard):
        for i in range(NUM_LEDS):
            pixels[i] = (50, 50, 50)
        pixels.show()
        time.sleep(0.1)
        clear_leds()
    
    def before_matrix_scan(self, keyboard):
        if self.timer is not None:
            if time.monotonic() - self.timer >= self.timeout:
                clear_leds()
                self.timer = None
                self.current_key = None
    
    def after_matrix_scan(self, keyboard):
        current_pressed = set()
        for i, key_state in enumerate(keyboard.matrix.get_pressed()):
            if key_state and i < 8:
                current_pressed.add(i)
        
        new_presses = current_pressed - self.last_pressed
        for key in new_presses:
            self.light_key(key)
        
        self.last_pressed = current_pressed
    
    def after_hid_send(self, keyboard):
        pass
    
    def on_powersave_enable(self, keyboard):
        clear_leds()
        self.timer = None
    
    def on_powersave_disable(self, keyboard):
        pass
    
    def light_key(self, key):
        clear_leds()
        
        if key in LED_MAP:
            color = LED_COLORS['double'] if len(LED_MAP[key]) > 1 else LED_COLORS['single']
            
            for led in LED_MAP[key]:
                pixels[led] = color
            pixels.show()
        
        self.current_key = key
        self.timer = time.monotonic()

led_timer = LEDTimerModule(timeout=2.0)
keyboard.modules.append(led_timer)

keyboard.keymap = [
    [
        KC.LWIN(KC.I),
        KC.LWIN(KC.E),
        KC.LWIN(KC.N1),
        KC.LWIN(KC.N2),
        KC.LWIN(KC.N3),
        KC.LWIN(KC.N4),
        KC.LWIN(KC.N5),
        KC.LCTL(KC.LSFT(KC.ESC)),
    ]
]

if __name__ == '__main__':
    keyboard.go()