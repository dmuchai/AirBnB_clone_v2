#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents 
of the web_static folder of my AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Generate timestamp for the archive name
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create versions folder if it doesn't exist
    local("mkdir -p versions")

    # Create the .tgz archive
    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result

if __name__ == "__main__":
    do_pack()
