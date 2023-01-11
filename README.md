# WaterSpy
A Raspberry Pi Pico application to sense the water level in a poultry fount.

This project was born of a quirky idea:  In the Winter, we need to put out watering founts in our chicken coop that won't freeze during cold snaps.  These are made of galvanized steel, and we sit them on top of heaters.  The problem is that we can't tell when they need to be refilled without going into the coop and picking them up. Laziness being the mother of invention, I sought a technical solution.

The main parts of this solution are a Raspberry Pi Pico and a HC-SR04 ultrasonic sensor.  The Python code listed here boots up the WiFi and a web server, and then uses jQuery (Javascript) to poll the sensor.  The result is displayed as a graphical representation of the fount showing the current water level.

![the fount](https://github.com/mpemburn/WaterSpy/blob/master/WaterSpy.png)
