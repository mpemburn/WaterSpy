import machine
import uasyncio as asyncio
import network
import time
import ubinascii

WLAN = network.WLAN(network.STA_IF)


def get_connection():
    return WLAN


async def connect_wifi(ssid, password):
    WLAN.active(True)
    WLAN.connect(ssid, password)
    MAC = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    LED = machine.Pin("LED", machine.Pin.OUT)

    LED.value(True)

    timeout = 0;
    while not WLAN.isconnected() and WLAN.status() >= 0:
        print("Attempting to connect to " + ssid)
        time.sleep(1)
        timeout = timeout + 1
        if timeout == 10:
            print("Connection timed out.  Aborting")
            return;

    LED.value(False)
    if WLAN.isconnected():
        print("Connected to " + ssid)
        print("IP Address:" + WLAN.ifconfig()[0])
        print("MAC Address: " + MAC.upper())


def connect(primary, secondary):
    asyncio.run(connect_wifi(primary["ssid"], primary["password"]))

    if WLAN.isconnected() != True:
        print("Unable to connect.  Trying fallback")
        asyncio.run(connect_wifi(secondary["ssid"], secondary["password"]))

    return WLAN.isconnected()

