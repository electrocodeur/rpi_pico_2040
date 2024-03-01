import machine, time

led = machine.Pin(25,machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
    print("fini")
    