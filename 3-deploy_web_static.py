#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import run, put, env
from os import path

env.hosts = ['54.173.140.10', '3.85.1.16']

def do_deploy(archive_path):
    """Function to distribute an archive to web servers."""
    if not path.exists(archive_path):
        return False
    
    try:
        arch_name = path.basename(archive_path)
        arch_no_ext = path.splitext(arch_name)[0]

        # Upload the archive to /tmp/ on the remote server
        put(archive_path, "/tmp/")

        # Create the release directory and extract the archive
        run("mkdir -p /data/web_static/releases/{}/".format(arch_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(arch_name, arch_no_ext))

        # Remove the uploaded archive from /tmp/
        run("rm /tmp/{}".format(arch_name))

        # Move contents from web_static subdirectory to the release directory
        run(("mv /data/web_static/releases/{}/web_static/* " +
            "/data/web_static/releases/{}/").format(arch_no_ext, arch_no_ext))

        # Remove the now-empty web_static subdirectory
        run("rm -rf /data/web_static/releases/{}/web_static/"
            .format(arch_no_ext))

        # Update the symbolic link to point to the new release
        run(("rm -rf /data/web_static/current && " +
            "ln -s /data/web_static/releases/{}/ /data/web_static/current")
            .format(arch_no_ext))

        return True
    except FileNotFoundError:
        print("Error: The archive file does not exist.")
        return False
    except Exception as e:
        print("Error: {}".format(e))
        return False
