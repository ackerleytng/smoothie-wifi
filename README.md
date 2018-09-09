# `smoothie-wifi`

A little web service to allow wifi configuration:

+ Select SSID
+ Enter password to connect

## Intended application

`smoothie-wifi` was designed to run on a raspberry pi (Zero W).

It will listen on the pi's bluetooth PAN, so users can connect to the
Bluetooth PAN and use this to configure the raspberry pi's wifi
interface.

If you follow the config in `config/bluetooth-pan`, the raspi's ip
will be `172.111.1.1`.