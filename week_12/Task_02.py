from machine import Pin
import tm1637
import time

display = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

current_time = time.localtime()
print(current_time)

# year = current_time[0]
# month = current_time[1]
# day = current_time[2]
# hour = current_time[3]
# minute = current_time[4]
# second = current_time[5]

minutes = 0
seconds = 0

# clear the display
clear_display = display.show("    ")

# Set brightness (0-7)
display.brightness(7)

minutes = 0
seconds = 0

while True:    
    # Display current time
    display.numbers(minutes, seconds, colon=True)
    
    # Wait .5 second
    time.sleep(.5)

    # Turn colon off
    display.numbers(minutes, seconds, colon=False)

    # Wait .5 second
    time.sleep(.5)
    
    # Increment seconds
    seconds = seconds + 1
    
    # Handle minute rollover
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1
    
    # Handle hour rollover
    if minutes > 99:
        minutes = 0