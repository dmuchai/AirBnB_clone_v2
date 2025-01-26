#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update and install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update -y
    apt-get install nginx -y
fi

# Create required directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link to /data/web_static/releases/test/
if [ -L /data/web_static/current ]; then
    rm -f /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
sed -i '/server_name _;/a \\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx restart

# Always exit successfully
exit 0
