# Deployment

### Install nginx
```bash
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install nginx -y
```

### `/etc/nginx/sites-available/fastapi-proxy`
- create
```bash
/etc/nginx/sites-available/fastapi-proxy
```

- content
```
server {
    listen 80;
    listen [::]:80;  # Remove if IPv6 unsupported
    server_name 172.234.163.116;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Create symbolic link
```bash
sudo ln -s /etc/nginx/sites-available/fastapi-proxy /etc/nginx/sites-enabled/fastapi-proxy
```


### Restart nginx
```bash
sudo systemctl restart nginx
```
