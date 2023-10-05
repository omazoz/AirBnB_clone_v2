#!/usr/bin/python3
"""Author: Talaini
  function do_pack that generates a .tgz archive"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """ Fabric script that generates a .tgz archive"""
    local("sudo mkdir -p versions")
    gndate = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(gndate)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
