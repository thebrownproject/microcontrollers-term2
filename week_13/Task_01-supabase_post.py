from time import sleep
import time
import dht
import network
import urequests
from machine import Pin

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
print(f"Temperature: {temperature}C, Humidity: {humidity}%")

def post_to_supabase():
    url = "https://dbdsuizkukzqbdistahu.supabase.co/rest/v1/weather_reading"
    data = {
        "temperature": temperature,
        "humidity": humidity,
    }

    headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRiZHN1aXprdWt6cWJkaXN0YWh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcxMDE2MjUsImV4cCI6MjA2MjY3NzYyNX0.O-DptITL6x3hAajT9qwglUYJjTk8vyqtKo7ZqFJYr9s",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRiZHN1aXprdWt6cWJkaXN0YWh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcxMDE2MjUsImV4cCI6MjA2MjY3NzYyNX0.O-DptITL6x3hAajT9qwglUYJjTk8vyqtKo7ZqFJYr9s",
    "Content-Type": "application/json"
    }

    try:
        response = urequests.post(url, json=data, headers=headers)
        print("Status code:", response.status_code)
        raw = response.text
        if raw and raw.strip():
            print("Response JSON:", response.json())
        else:
            print("Data posted successfully! (No response body returned)")
        response.close()
    except Exception as e:
        print("Failed to post data:", e)

post_to_supabase()




