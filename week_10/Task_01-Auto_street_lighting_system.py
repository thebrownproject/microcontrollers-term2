from machine import Pin, ADC
import time

led = Pin(2, Pin.OUT)
ldr = ADC(Pin(26))

while True:
    if ldr.read_u16() > 15000:
        print(f"Night Time: Light are OFF - Sensor value: {ldr.read_u16()}")
        led.off()
        time.sleep(1)
    else:
        print(f"Day Time: Light are ON - Sensor value: {ldr.read_u16()}")
        led.on()
        time.sleep(1)

