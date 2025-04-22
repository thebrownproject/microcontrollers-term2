from machine import Pin, ADC
import time

pir = ADC(Pin(26))  # PIR sensor
led = Pin(2, Pin.OUT)  # LED

while True:
    sensor_value = pir.read_u16()

    if sensor_value > 17000:
        led.on()
        print(f"Motion detected! Light on. Sensor value: {sensor_value}")
        time.sleep(3)
    else:
        print(f"No motion detected. Light off. Sensor value: {sensor_value}")
        led.off()