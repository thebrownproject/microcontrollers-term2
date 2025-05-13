from mfrc522 import MFRC522
import time
import network
import urequests

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

ssid = "CyFi"
password = "SecurityA40"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected!", station.ifconfig())


first_name = "Luca"
last_name = "T"

def post_to_supabase(card_id):
    url = "https://dbdsuizkukzqbdistahu.supabase.co/rest/v1/rfid_reading"
    data = {
        "card_id": card_id,
        "first_name": first_name,
        "last_name": last_name,
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

print("Bring TAG closer...")
print("")

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print(f"Card ID: {card}")
            post_to_supabase(card)
        time.sleep_ms(500)

