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

def fetch_data_supabase(id):
    url = f"https://dbdsuizkukzqbdistahu.supabase.co/rest/v1/weather_reading?id=eq.{id}"
    headers = {
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRiZHN1aXprdWt6cWJkaXN0YWh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcxMDE2MjUsImV4cCI6MjA2MjY3NzYyNX0.O-DptITL6x3hAajT9qwglUYJjTk8vyqtKo7ZqFJYr9s",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRiZHN1aXprdWt6cWJkaXN0YWh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcxMDE2MjUsImV4cCI6MjA2MjY3NzYyNX0.O-DptITL6x3hAajT9qwglUYJjTk8vyqtKo7ZqFJYr9s",
        "Content-Type": "application/json"
    }
    try:
        response = urequests.get(url, headers=headers)
        data = response.json()
        print("Data received from Supabase:", data)
        response.close()
    except Exception as e:
        print("Failed to fetch data:", e)

fetch_data_supabase(3)


