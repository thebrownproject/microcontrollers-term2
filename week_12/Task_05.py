from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import hcsr04
from time import sleep
import time

led_red = Pin(15, Pin.OUT)
led_green = Pin(16, Pin.OUT)
led_blue = Pin(17, Pin.OUT)

led_green.off()
led_blue.off()
led_red.off()

buzzer = PWM(Pin(15))

sensor = hcsr04.HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=1000000)

def buzzer_sound():
    if distance_int > 100:
        buzzer.duty_u16(0)  # Turn off the buzzer
        return

    freq = 2000 - (distance_int * 15)
    if freq < 500:
        freq = 500

    interval = distance_int / 100
    if interval < 0.04:
        buzzer.duty_u16(20000)
        led_blue.on()
        oled.text("Danger!", 0, 20)
        time.sleep(.5)
        led_blue.off()
    else:
        buzzer.duty_u16(20000)
        buzzer.freq(freq)
        led_green.on()
        time.sleep(interval)
        buzzer.duty_u16(0)
        led_green.off()
        time.sleep(interval)


# Setup I2C connection
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

oled.fill(0)


while True:
    distance = sensor.distance_cm()
    distance_int = int(distance)

    oled.text(f"Distance:", 0, 0)
    oled.text(f"{distance_int} cm", 0, 10)

    if distance_int < 100:
        buzzer_sound()
    
    oled.show()
    sleep(0.1)
    oled.fill(0)