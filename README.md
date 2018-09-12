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

## Implementation

This is a wrapper around

+ `iwconfig`
+ `wpa_supplicant`

It assumes that the above are installed and running as set up on a raspi.

## Supported Wireless Configurations

Hope this grows! Let me know if you need something in particular.

+ WPA-PSK

```
network={
        ssid="the ssid"
        psk="the key"
        key_mgmt=WPA-PSK
}
```

## Developing on the pi

Syncing files over

```
rsync -avzh . pi@172.111.1.1:smoothie-wifi
```

Activating the virtualenv on the pi

```
$ cd ~
$ . venv/bin/activate
```
