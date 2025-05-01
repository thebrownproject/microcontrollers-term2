# Import libraries
from machine import Pin 
import time
import dht

# Define pins
led_green = Pin(14, Pin.OUT)
led_blue = Pin(13, Pin.OUT)
led_red = Pin(12, Pin.OUT)
DHT = dht.DHT11(Pin(16))

# Function to read temperature and humidity
while True:
    DHT.measure()
    temperature = DHT.temperature()
    humidity = DHT.humidity()
    print(f"Temperature: {temperature}C, Humidity: {humidity}%")
    for led in [led_green, led_blue, led_red]:
        led.off()
    if temperature > 30:
        print("Room is hot")
        led_red.on()
    elif temperature < 20:
        print("Room is cold")
        led_blue.on()
    else:
        print("Room is normal")
        led_green.on()
    time.sleep(2)
    


# loop through green, blue and red LEDs
# for led in [led_green, led_blue, led_red]:
#     led.off()
#     time.sleep(1)
#     led.on()
#     time.sleep(1)
#     led.off()



# DHT11 Sensor to read temperature and humidity

# If roomm is hot, RGB LED will be red

# If room is cold, RGP LED will be blue

# If room is normal, RGB LED will be green
