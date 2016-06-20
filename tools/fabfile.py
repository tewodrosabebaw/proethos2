#!coding:utf-8
from fabric.api import env, local, settings, abort, run, cd
from fabric.operations import local, put, sudo, get
from fabric.context_managers import prefix
from fabenv import *

from glob import iglob
import os

env.use_ssh_config = True

def update():

    with prefix(". %s" % env.env_script):
        with cd(env.path):
            run("git pull origin master")
            run("composer.phar update")
            
        with cd(env.symfony_path):
            run("php app/console doctrine:schema:update --force")
            run("php app/console proethos2:load-database-initial-data")
            