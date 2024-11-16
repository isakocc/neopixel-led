import time
from rpi_ws281x import *
import argparse
import signal

# LED strip configuration:
LED_COUNT = 1        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def off(signum, frame):
    colorWipe(strip, Color(0, 0, 0), 10)
    exit(0)

def brighten():
    for j in range(25, 255, 10):
        print(j)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(j,j,j))
        strip.show()
        time.sleep(0.04)

def darken():
    for j in range(255, 25, -10):
        print(j)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(j,j,j))
        strip.show()
        time.sleep(0.04)

signal.signal(signal.SIGTERM, off) 

if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')


    try:

        while True:
            brighten()
            time.sleep(0.3)
            darken()
            time.sleep(0.05)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
