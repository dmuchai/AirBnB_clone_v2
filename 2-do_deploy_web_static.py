#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.
"""
from fabric.api import env, put, run
import os

# Define the web servers
env.hosts = ['34.234.193.82', '18.214.89.239']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): The path to the archive file.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get the archive name and its base name without extension
        archive_name = os.path.basename(archive_path)
        base_name = os.path.splitext(archive_name)[0]

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, f"/tmp/{archive_name}")

        # Create the release folder
        run(f"mkdir -p /data/web_static/releases/{base_name}/")

        # Uncompress the archive to the release folder
        run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{base_name}/")

        # Remove the uploaded archive from the web server
        run(f"rm /tmp/{archive_name}")

        # Move the content out of the web_static subdirectory
        run(f"mv /data/web_static/releases/{base_name}/web_static/* /data/web_static/releases/{base_name}/")

        # Remove the now-empty web_static folder
        run(f"rm -rf /data/web_static/releases/{base_name}/web_static")

        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the release folder
        run(f"ln -s /data/web_static/releases/{base_name}/ /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False


if __name__ == "__main__":
    archive_path = "versions/web_static_20170315003959.tgz"  # Example path
    do_deploy(archive_path)
