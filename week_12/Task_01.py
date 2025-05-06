from machine import Pin
import tm1637
import time

display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

current_time = time.localtime()
print(current_time)

year = current_time[0]
month = current_time[1]
day = current_time[2]
hour = current_time[3]
minute = current_time[4]
second = current_time[5]


# clear the display
display.show("    ")

# Set brightness (0-7)
display.brightness(7)
while True:
    display.numbers(hour, minute, colon=True)
    print(hour, minute)
    time.sleep(.5)
    display.numbers(hour, minute, colon=False)
    time.sleep(.5)