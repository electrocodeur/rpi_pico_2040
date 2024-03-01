from machine import * 
from time import * 
from neopixel import NeoPixel
from random import *
NUMBER_PIXELS = 1
LED_PIN = 23

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

button = Pin(24, Pin.IN, Pin.PULL_UP)
while True:
    etat = button.value()
    if etat == 0:
        print("Le bouton est pressé")
        nbr = randint(0,255)
        nbv = randint(0,255)
        nbb = randint(0,255)
        strip[0] = (nbr,nbv,nbb) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
    sleep(0.1)
