# Config for bluetooth PAN

| File               | Path on raspi                          | Purpose                               |
| ---                | ---                                    | ---                                   |
| pan0.netdev        | /etc/systemd/network/pan0.netdev       | Creates a pan0 network interface      |
| pan0.network       | /etc/systemd/network/pan0.network      | Starts a network on pan0              |
| bt-network.service | /etc/systemd/system/bt-network.service | Provides a network?                   |
| bt-agent.service   | /etc/systemd/system/bt-agent.service   | Starts agent to handle authentication |

# Start these services

```
sudo systemctl enable systemd-networkd
sudo systemctl enable bt-agent
sudo systemctl enable bt-network
sudo systemctl start systemd-networkd
sudo systemctl start bt-agent
sudo systemctl start bt-network
```


# Bluetooth configuration

I had to make bluetooth always be discoverable, so that a user can
always connect to it. (User will not have a mouse/keyboard attached to
the raspi)

Uncomment these two in `/etc/bluetooth/main.conf`

```
DiscoverableTimeout = 0
PairableTimeout = 0
```

# Other commands

Set bluetooth to be discoverable

```
sudo hciconfig hci0 piscan
```

Set bluetooth alias

```
sudo hciconfig hci0 name smoothie
```

Change bluetooth name: `/etc/bluetooth/main.conf` uses the hostname,
so edit `/etc/hosts` and `/etc/hostname` to change the hostname to
whatever you prefer.
