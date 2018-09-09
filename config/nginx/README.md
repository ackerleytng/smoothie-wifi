# Config for nginx

| File          | Path on raspi                            | Purpose                                    |
| ---           | ---                                      | ---                                        |
| smoothie.conf | /etc/nginx/sites-available/smoothie.conf | nginx config to proxy requests to gunicorn |

# Start these services

```
sudo systemctl restart nginx
```
