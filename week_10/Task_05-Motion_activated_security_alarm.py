from machine import Pin, ADC, PWM
import time

led = Pin(2, Pin.OUT)  # LED
pir = ADC(Pin(26))  # PIR sensor
buzzer = PWM(Pin(15), freq=1000)  # Buzzer

alarm_sound_freq = [1000, 1500, 1000, 1500, 1200, 1700]  # Frequencies for alarm sound

def sound_alarm():
    for freq in alarm_sound_freq:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)  # Set duty cycle to 50%
        time.sleep(0.1)  # Duration of each frequency
    buzzer.duty_u16(0)  # Turn off the buzzer


while True:
    # Read the PIR sensor value
    sensor_value = pir.read_u16()
    print(f"Sensor value: {sensor_value}")
    time.sleep(.2)
    # Check if motion is detected
    if sensor_value > 16000:
        # Turn alarm system on
        print(f"Motion detected! Alarm system on!. Sensor value: {sensor_value}")
        for i in range(5):
            led.on()
            sound_alarm()
            time.sleep(0.1)
            led.off()
            time.sleep(0.1)
        # Turn alarm system off
        led.off()
        buzzer.duty_u16(0)
        print(f"No motion detected. Alarm system off! Sensor value: {sensor_value}")
