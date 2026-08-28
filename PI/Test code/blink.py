import machine
import neopixel
from utime import sleep

# Configure the WS2812 RGB LED on GPIO 16 (1 pixel)
np = neopixel.NeoPixel(machine.Pin(16), 1)

print("LED starts flashing white...")

while True:
    try:
        # Toggle between White (255, 255, 255) and Off (0, 0, 0)
        if np[0] == (0, 0, 0):
            np[0] = (255, 255, 255)  # White
        else:
            np[0] = (0, 0, 0)        # Off

        np.write()
        sleep(1)
    except KeyboardInterrupt:
        break

# Turn off LED on exit
np[0] = (0, 0, 0)
np.write()
print("Finished.")