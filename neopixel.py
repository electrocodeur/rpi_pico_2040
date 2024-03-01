from machine import Pin
from time import sleep
from neopixel import NeoPixel
from random import *

NUMBER_PIXELS = 1
LED_PIN = 23

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

while True:
    nbr = randint(0,255)
    nbv = randint(0,255)
    nbb = randint(0,255)
    strip[0] = (nbr,nbv,nbb) # red=255, green and blue are 0
    strip.write() # send the data from RAM down the wire
    print(nbr)
    print(nbv)
    print(nbb)
    sleep(1)