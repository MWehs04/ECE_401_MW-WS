import machine
import neopixel
from utime import sleep

# Configure the WS2812 RGB LED on GPIO 16 (1 pixel)
np = neopixel.NeoPixel(machine.Pin(16), 1)
Buzzer = machine.Pin(8, machine.Pin.OUT)
print("print test")

while True:
    for i in range(3):  # Flash 3 times
        for i in range(3):  # Flash 3 times
            Buzzer.value(1)  # Turn on buzzer
            sleep(0.5)  # Wait for 0.5 seconds
            Buzzer.value(0)  # Turn off buzzer
            sleep(.75)
        sleep(3)
    sleep(1500)

print("Finished.")

#will was here