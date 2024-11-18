import board
import neopixel
import argparse
import signal
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import *

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D18
# Update to match the number of NeoPixels you have connected
pixel_num = 2

ORDER = neopixel.GRB

def wipe():
    pixels.fill((0, 0, 0))
    pixels.show()

def off(signum, frame):
    pixels.fill((0, 0, 0))
    pixels.show()
    exit(0)

signal.signal(signal.SIGTERM, off)


if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=1, auto_write=False, pixel_order=ORDER)

    pulse = Pulse(pixels, speed=0.01, color=AMBER, period=1.8, min_intensity=0.2)


    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            pulse.animate()

    except KeyboardInterrupt:
        if args.clear:
            wipe()
