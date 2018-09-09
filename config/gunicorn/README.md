# Config for `smoothie-wifi`

| File                  | Path on raspi                              | Purpose                             |
| ---                   | ---                                        | ---                                 |
| smoothie-wifi.service | /etc/systemd/network/smoothie-wifi.service | Starts gunicorn to serve falcon app |

# Start these services

```
sudo systemctl enable smoothie-wifi
sudo systemctl start smoothie-wifi
```
