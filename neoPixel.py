
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def flash(color, flashtime):
    num= 5
    for n in range(num):
        a=color[0]/n
        b=color[1]/n
        c=color[2]/n
        pixels.fill((a,b,c))
        pixels.show
        time.sleep(flashtime/5)
        
        #pixels.fill(color/5)
'''

def pulse_to_energy(spotifyObject):
    while True:
        energy = spotify_part.get_energy(spotifyObject)
        
        if energy is None:
            print("No song is currently playing.")
            time.sleep(5)
            continue

        if energy > 0.5:
            pulse_speed = 0.1  
            max_brightness = 0.8  
        else:
            pulse_speed = 0.3  
            max_brightness = 0.5  

        #Increases brightness.
        for brightness in range(0, int(max_brightness * 100), 5):
            pixels.brightness = brightness / 100.0
            pixels.fill((0, 255, 0))  #TODO find a way to fill 
            time.sleep(pulse_speed)

        # Gradually decrease brightness (pulse off)
        for brightness in range(int(max_brightness * 100), 0, -5):
            pixels.brightness = brightness / 100.0
            pixels.fill((0, 255, 0))  # Bright green
            time.sleep(pulse_speed)
'''