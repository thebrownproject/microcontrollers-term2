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

def fetch_data():
        url = "https://681d50bef74de1d219af6197.mockapi.io/api/v1/newuser"
        try:
            response = urequests.get(url)
            data = response.json()
            
            print("Data received from MockAPI:", response)
            for entries in data:
                print(entries)
                  
        except Exception as e:
            print("Failed to fetch data:", e)
    
fetch_data()