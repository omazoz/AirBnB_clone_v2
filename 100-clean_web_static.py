#!/usr/bin/python3
""" Author: Talaini
    deletes out-of-date archives, using the function"""
from fabric.api import *


env.hosts = ['54.89.109.168', '54.157.141.86']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS number of the archives, including the most recent, to keep """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))