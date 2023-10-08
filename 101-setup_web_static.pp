#Author Mazoz
#Script that configures Nginx server with some static html
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> exec { 'create data':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}
-> exec { 'index':
  command => '/usr/bin/echo "Hi!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}
-> exec { 'remove current':
  command => '/usr/bin/rm -rf /data/web_static/current',
}
-> exec { 'simbolic':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'chmod data':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}
-> exec { 'hbnb_static':
  command => 'sudo sed -i "/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}" /etc/nginx/sites-enabled/default',
  provider => shell,
}
-> exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
