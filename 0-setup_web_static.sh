#!/usr/bin/env bash
# This script sets up the web servers for deploying web_static

# Exit on error
set -e

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories with the correct permissions
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chmod -R 755 /data

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create (or recreate) the symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of the /data directory to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve /hbnb_static
sudo sed -i "/server_name _;/a\\
    location /hbnb_static/ {\n\
        alias /data/web_static/current/;\n\
        index index.html;\n\
    }" /etc/nginx/sites-available/default

# Test and restart Nginx
sudo nginx -t
sudo service nginx restart

# Exit successfully
exit 0
