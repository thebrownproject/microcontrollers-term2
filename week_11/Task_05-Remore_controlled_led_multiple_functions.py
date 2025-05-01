from machine import Pin, time_pulse_us
from time import sleep

ir = Pin(22, Pin.IN, Pin.PULL_UP)
led_green = Pin(14, Pin.OUT)
led_state = False


print("Point your remote at the IR receiver and press a button…")

while True:
    # ——— Detect start of a button press ———
    # The IR receiver output idles HIGH; pressing any key pulls it LOW.
    
    while ir.value() == 1:
        pass  # wait here until it goes LOW

    # ——— the sync pulses ———
    time_pulse_us(ir, 0)  # wait out the long LOW
    time_pulse_us(ir, 1)  # wait out the long HIGH

    
    for _ in range(16):
        time_pulse_us(ir, 0)  # skip each short LOW
        time_pulse_us(ir, 1)  # skip each short HIGH

    # ——— Read the 8 bits of the command byte ———
    command = 0
    for bit in range(8):
        time_pulse_us(ir, 0)         
        high_time = time_pulse_us(ir, 1)  
        
        if high_time > 1000:
            command |= 1 << bit     # set this bit to 1

    # ——— Print the result ———
    print("Button code =", hex(command))

    if command == 0x0:
        led_state = not led_state
        if led_state:
            for i in range(8):
                led_green.on()
                sleep(.1)
                led_green.off()
                sleep(.1)
                led_green.on()

        else:
            led_green.off()

    # tiny pause so repeats are clean
    sleep(0.3)