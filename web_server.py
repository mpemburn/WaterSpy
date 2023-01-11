# web_server.py

import socket
import wifi
import time
import file_loader
import read_sensor

wlan = wifi.get_connection()

css = file_loader.get('style.css')

script = file_loader.get('script.js')

html = """<!DOCTYPE html>
<html>
    <head>
        {0}
        <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>
        {1}
        <title>Water Spy</title>
    </head>
    <body>
        <div style="width: 50%; margin-top: text-align: center; block-size: fit-content;">
            <h1>Water Level</h1>
            <p id="output"></p>
            <div id="image">
            </div>
            <div class="cylinder">
                <div class="water"></div>
            </div>

        </div>
    </body>
</html>
"""
html = html.format(css, script)

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
        client, addr = s.accept()
        # print('client connected from', addr)
        request = client.recv(1024)
        # print(request)

        request = str(request)
        image = request.find('/get_image')
        sensor = request.find('/get_sensor')

        if image == 6:
            response = str(file_loader.get('waterer.svg'))
        elif sensor == 6:
            response = str(read_sensor.read())
        else:
            response = html

        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(response)
        client.close()

    except OSError as e:
        client.close()
        print('connection closed')

