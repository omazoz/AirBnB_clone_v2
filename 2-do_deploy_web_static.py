#!/usr/bin/python3
"""Author: Talaini
   a Fabric script that distributes an archive to  web servers"""


from fabric.api import *
from datetime import datetime
from os.path import exists

"<IP web-01>, <IP web-02>"
env.hosts = ['54.89.109.168', '54.157.141.86']


def do_deploy(archive_path):
    """ deploy an archive to  servers
    """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        return True
    except BaseException:
        return False
