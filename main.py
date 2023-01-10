import secrets
import wifi

## Get the WiFi running
if wifi.connect(secrets.MAIN, secrets.SECOND):
    print("WiFi connected.")
    import web_server
else:
    print("Unable to connect to WiFi.")
