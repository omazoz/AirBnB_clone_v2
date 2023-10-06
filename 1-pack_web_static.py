#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function to generate a .tgz archive from web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date)
    file_path = os.path.join("versions", file_name)
    print("Packing web_static to {}".format(file_path))

    try:
        local("tar -czvf {} -C web_static .".format(file_path))
        file_size = os.path.getsize(file_path)
        print("web_static packed: {} -> {} Bytes".format(file_path, file_size)) 
        return file_path
    except Exception as e:
        print("Error: {}".format(e))
        return None
