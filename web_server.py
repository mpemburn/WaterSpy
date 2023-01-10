import network
import socket
import wifi
import time
import file_loader
import read_sensor

from machine import Pin

wlan = wifi.get_connection()

css = file_loader.get('style.css')

script = file_loader.get('script.js')

head = """<!DOCTYPE html>
<html>
    <head>
        {0}
        <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>
        {1}
        <title>Water Spy</title>
    </head>
    <body>
        <div style="width: 50%; margin-top: text-align: center;">
            <h1>Water Level</h1>
            <p id="output"></p>
            <div class="cylinder">
                <div class="water"></div>
            </div
        <div>
            """
tail = """
            </div>
        </div>
    </body>
</html>
"""
html = head.format(css, script) + tail

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

addr = socket.getaddrinfo('0.0.0.0', 8008)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        # print('client connected from', addr)
        request = cl.recv(1024)
        # print(request)

        request = str(request)
        sensor = request.find('/get_sensor')

        if sensor == 6:
            response = str(read_sensor.read())

        else:
            response = html

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')