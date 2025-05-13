import network
import time
import urequests

DHT = dht.DHT11(Pin(16))
DHT.measure()
temperature = DHT.temperature()
humidity = DHT.humidity()

ssid = "CyFi"
password = "SecurityA40"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected!", station.ifconfig())

