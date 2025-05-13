from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import hcsr04
from time import sleep
import time

# Setup I2C connection
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Connect a buzzer to Pin 15
buzzer = PWM(Pin(15))

def buzzer_sound():
    buzzer.duty_u16(20000)  # Set duty cycle for sound output
    frequencies = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    
    for freq in frequencies:
        buzzer.freq(freq)  # Set frequency for buzzer
        time.sleep(0.05)
    
    buzzer.duty_u16(0)  # Turn off the buzzer





# Clear the screen
oled.fill(0)

sensor = hcsr04.HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=1000000)

# Display time
while True:        
    # Print distance
    distance = sensor.distance_cm()
    distance_int = int(distance)
    oled.text("Distance:", 0, 0)
    if distance_int < 100:
        oled.text(f"{distance_int} cm", 0, 10)
        oled.show()
        if distance_int < 10:
            buzzer_sound()
    else:
        oled.text("", 0, 10)
        oled.show()
    sleep(.2)
    oled.fill(0)