# dnsmasq

We do this so that users can surf to `smoothie.wifi` after connecting to bluetooth

## Config for dnsmasq

| File               | Path on raspi                          | Purpose                               |
| ---                | ---                                    | ---                                   |
| dnsmasq.conf       | /etc/dnsmasq.conf                      | dnsmasq config                        |
| dnsmasq.hosts      | /etc/dnsmasq.hosts                     | Static dns entries for dnsmasq        |

## Start these services

```
sudo systemctl enable dnsmasq
sudo systemctl start dnsmasq
```
