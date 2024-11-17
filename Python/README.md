#Python implementation for raspberry pi:

The file fade-sigterm-ws281x.py uses rpi-ws281x library and make led fade in and out in white color using strip.setPixelColor function to set the color and change brightness by changing 32 bit color information in the function (from Color(255,255,255) to Color(25,25,25) and back) with a range() function (that is strip.setPixelColor(i, Color(j,j,j) where j is in a range of 25 to 255). To resolve that I used this discussion (also see this implementation in the Arduino section): https://forum.arduino.cc/t/adafruit-neopixel-code-for-simple-brightness-fade/418170/7. It clears all leds when finishing script with ctrl-c (for that you need to start the script using -c argument: fade-sigterm-ws281x.py -c) or when system shuts down (for that you need to add script to start at boot with crontab -e: @reboot sudo python /"location of file"/fade-sigterm-ws281x.py & ).

The file fade-color-sigterm-ws281x.py uses rpi-ws281x library and make led fade in and out in a defined color using strip.setBrightness function to change brightness by changing 32 bit brightness information in the function (from strip.setBrightness(255) to strip.setBrightness(25)  and back) with a range() function (that is strip.setBrightness(j) where j is in a range of 25 to 255). To change to the desired color you need to set it in lines 68 and 70 in a GRB format (see color-grb.py for a list of colors in that format). It clears all leds when finishing script with ctrl-c (for that you need to start the script using -c argument: fade-color-sigterm-ws281x.py -c) or when system shuts down (for that you need to add script to start at boot with crontab -e: @reboot sudo python /"location of file"/fade-color-sigterm-ws281x.py & ).

I used the "sigterm" approach from https://dev.to/khenhey/light-up-leds-when-you-start-your-raspberry-pi-and-clear-them-on-shutdown-542

As Raspberry Pi 5 is not supporting either ws281x and Adafruit-Neopixel library at the moment, it would have to be implemented with Pi5Neo library (see https://pypi.org/project/Pi5Neo/). I reproduce one approach in the examples of the library (can't test because I dont have a rpi5 here): fade-Pi5Neo.py

For the Adafruit Neopixel library the approach would be adding Adafruit_CircuitPython_LED_Animation library to use the pulse.animate() function. To install system-wide:

sudo pip3 install adafruit-circuitpython-led-animation

Additional you would have to change the color.py file to match colors in a GRB format. Download color-grb.py and copy it to /usr/local/lib/python3.11/dist-packages/adafruit_led_animation/. Then change the names of files:

mv color.py color.py.old
mv color-grb.py color.py

This implementation is in the script pulse.py. 
