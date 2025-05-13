import network
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

def post_data():
    url = "https://681d50bef74de1d219af6197.mockapi.io/api/v1/newuser"
    data = {
        "name": "Fraser B",
        "city": "West Melbourne",
        "country": "Australia",
    }
    try:
        response = urequests.post(url, json=data)
        print("Data posted to MockAPI:")
        print(response.json())
    except Exception as e:
        print("Failed to post data:", e)

post_data()