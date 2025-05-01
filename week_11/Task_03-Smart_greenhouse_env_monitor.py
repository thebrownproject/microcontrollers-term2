from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import time
import dht

# Setup I2C connection
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

DHT = dht.DHT11(Pin(16))
DHT.measure()
temperature = DHT.temperature()
humidity = DHT.humidity()

# Clear the screen
oled.fill(0)


# Display time
while True:        
    current_time = time.localtime()
    oled.text(f"Time: {current_time[3]}:{current_time[4]}:{current_time[5]}", 0, 0)
    oled.text(f"Date: {current_time[2]}.{current_time[1]}.{current_time[0]}", 0, 10)
    oled.text(f"Temp: {temperature}C", 0, 20)
    oled.text(f"Humi: {humidity}%", 0, 30)
    oled.show()
    sleep(1)
    oled.fill(0)