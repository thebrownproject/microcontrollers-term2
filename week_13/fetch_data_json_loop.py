import network
import time
import urequests

ssid = "CyFi"
password = "SecurityA40"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected!", station.ifconfig())

album_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
albums = []

for album_id in album_ids:
    response = urequests.get(f'http://jsonplaceholder.typicode.com/albums/{album_id}')
    data = response.json()
    albums.append(data)
    response.close()
    print(albums)

print(albums)