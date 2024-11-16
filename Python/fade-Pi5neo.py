#Reproduced from the examples in the package https://files.pythonhosted.org/packages/45/b6/c8d24e7306d7c6e670086c7f7c2c9dd3ae596a20b82aee3ce839ced2dd7f/pi5neo-1.0.5.tar.gz
#Breathing Effect for a Single LED (LED slowly fades in and out)
import time
from pi5neo import Pi5Neo

def breathing_led(neo, led_index, color, steps=50, delay=0.05):
    for i in range(steps):
        intensity = int(255 * (i / steps))  # Gradually increase intensity
        neo.set_led_color(led_index, *(intensity if c > 0 else 0 for c in color))  # Adjust brightness
        neo.update_strip()
        time.sleep(delay)
    for i in range(steps, 0, -1):
        intensity = int(255 * (i / steps))  # Gradually decrease intensity
        neo.set_led_color(led_index, *(intensity if c > 0 else 0 for c in color))
        neo.update_strip()
        time.sleep(delay)

# Initialize Pi5Neo with 10 LEDs
neo = Pi5Neo('/dev/spidev0.0', 10, 800)

# Breathing effect on 1st LED with red color
breathing_led(neo, 0, (255, 0, 0))
