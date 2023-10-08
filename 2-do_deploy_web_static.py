#!/usr/bin/python3
"""Author: omazoz
   a Fabric script that distributes an archive to  web servers"""


from fabric.api import *
from datetime import datetime
from os.path import exists
import os
"<IP web-01>, <IP web-02>"
env.hosts = ['54.173.140.10', '3.85.1.16']


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


def do_deploy(archive_path):
    """ deploy an archive to  servers
    """
    if exists(archive_path) is False:
        return False
    try:
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
