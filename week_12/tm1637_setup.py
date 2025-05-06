from machine import Pin
import tm1637
import time

display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

# Set brightness (0-7)
display.brightness(7)
while True:
    # Display a number
    display.number(2025)
    time.sleep(2)

    # Display a custom string ()
    display.show("HIII")
    time.sleep(2)
    display.scroll("HELLO 2025")
    time.sleep(0.1)


