#!/usr/bin/python3
"""Deploy archive"""

from fabric.api import *
from os.path import exists, splitext, basename

env.hosts = ['100.26.9.167', '52.201.179.163']


@task
def do_deploy(archive_path):
        """Fabric script that distributes an archive to your web servers"""
        if not exists(archive_path):
                return False
        try:
                archive_name = basename(archive_path)
                archive_ext = splitext(archive_name)[0]
                tmp_path = "/tmp/{}".format(archive_name)
                data_path = "/data/web_static/releases/{}".format(archive_ext)
                # Fabric commands
                put(archive_path, '/tmp/')
                run('mkdir -p {}'.format(data_path))
                run('tar -xzf {}  -C {}'.format(tmp_path, data_path))
                run('rm {}'.format(tmp_path))
                run('mv {}/web_static/* {}/'.format(data_path, data_path))
                run('rm -rf {}/web_static'.format(data_path))
                run('rm -rf /data/web_static/current')
                run('ln -s {} /data/web_static/current'.format(data_path))
                print("New version deployed!")
                return True
        except Exception as e:
                return False