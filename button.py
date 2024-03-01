import machine
import time
button = machine.Pin(24, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    etat = button.value()
    if etat == 0:
        print("Le bouton est pressé")
    time.sleep(0.1)
