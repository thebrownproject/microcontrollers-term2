from machine import Pin, ADC, PWM
import time

adc = ADC(Pin(26))  # LDR

led_red = PWM(Pin(12, Pin.OUT), freq=1000)
led_green = PWM(Pin(13, Pin.OUT), freq=1000)
led_blue = PWM(Pin(14, Pin.OUT), freq=1000)

def rgb_value_to_pwm(value):
    # Convert the RGB value (0-255) to a duty cycle (0-65535)
    return int(value * 65535 / 255)

while True:
    # Read the LDR value
    ldr_value = adc.read_u16()

    if ldr_value > 15000:
        # Night time: turn on the red LED
        led_red.duty_u16(rgb_value_to_pwm(255))
        led_green.duty_u16(rgb_value_to_pwm(100))
        led_blue.duty_u16(rgb_value_to_pwm(0))
        print(f"Night Time: Red LED ON - Sensor value: {ldr_value}")
        time.sleep(1)
    elif ldr_value > 10000:
        led_red.duty_u16(rgb_value_to_pwm(200))
        led_green.duty_u16(rgb_value_to_pwm(200))
        led_blue.duty_u16(rgb_value_to_pwm(255))
        print(f"Day Time: Green LED ON - Sensor value: {ldr_value}")
        time.sleep(1)
    else:
        led_red.duty_u16(rgb_value_to_pwm(0))
        led_green.duty_u16(rgb_value_to_pwm(255))
        led_blue.duty_u16(rgb_value_to_pwm(128))
        print(f"Bright room: Blue LED ON - Sensor value: {ldr_value}")
        time.sleep(1)



# while True:
#     led_red.on()
#     time.sleep(1)
#     led_red.off()
#     time.sleep(1)
#     led_green.on()
#     time.sleep(1)
#     led_green.off()
#     time.sleep(1)
#     led_blue.on()
#     time.sleep(1)
#     led_blue.off()
#     time.sleep(1)