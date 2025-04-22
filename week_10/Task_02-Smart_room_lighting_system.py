from machine import Pin, ADC, PWM
import time

led = PWM(Pin(2), freq=1000)
ldr = ADC(Pin(26))



while True:
    led.duty_u16(ldr.read_u16() * 2)  # Start with LED off
    print(f"Sensor value: {ldr.read_u16() * 2}")
    time.sleep(1)