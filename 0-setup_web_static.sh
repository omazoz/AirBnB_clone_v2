#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart