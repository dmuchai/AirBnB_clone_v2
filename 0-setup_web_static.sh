#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Exit on error
set -e

# Update and install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update -y
    apt-get install nginx -y
fi

# Create required directories with correct permissions
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" > /data/web_static/releases/test/index.html

# Remove existing symbolic link and create a new one
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership of /data/ to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sed -i '/server_name _;/a \\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n        index index.html;\n    }' /etc/nginx/sites-available/default
fi

# Test and restart Nginx to apply changes
nginx -t
service nginx restart

# Always exit successfully
exit 0
