#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.
"""
from datetime import datetime
from fabric.api import * 
import os

# Define the web servers
env.hosts = ["34.234.193.82", "18.214.89.239"]
env.user = "ubuntu"

def do_pack():
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): The path to the archive file.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result

def do_deploy(archive_path):
    """Deploy archive"""
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                            newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
