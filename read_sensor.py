from machine import Pin
import time

trigger = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)


def read():
    trigger.value(False)
    time.sleep(0.1)

    trigger.value(True)
    time.sleep_us(2)

    trigger.value(False)

    while echo.value() == False:
        pulse_start = time.ticks_us()
    while echo.value() == True:
        pulse_end = time.ticks_us()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    centimeters = round(distance, 0)
    inches = centimeters / 2.54

    return 'Distance:', "{:.2f}".format(inches), 'in'

