from machine import Pin
import time
import tm1637

display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))
display.brightness(7)

minutes = 0
seconds = 0
running = False

button_start = Pin(12, Pin.IN, Pin.PULL_UP)
button_stop = Pin(13, Pin.IN, Pin.PULL_UP)

def start_handler(pin):
    global running
    time.sleep_ms(20)
    if pin.value() == 0:
        running = True
        print("Stopwatch started")

def stop_handler(pin):
    global running
    time.sleep_ms(20)
    if pin.value() == 0:
        running = False
        print("Stopwarch stopped")

button_start.irq(trigger=Pin.IRQ_FALLING, handler=start_handler)
button_stop.irq(trigger=Pin.IRQ_FALLING, handler=stop_handler)

def update_display():
    global minutes, seconds

    display.numbers(minutes, seconds, colon=True)
    time.sleep(0.5)
    display.numbers(minutes, seconds, colon=False)
    time.sleep(0.5)

    if running:
        # Increment seconds
        seconds = seconds + 1
        # Handle minute rollover
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        # Handle hour rollover
        if minutes > 99:
            minutes = 0

while True:
    update_display()