import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

project_dir = 'sshtest'
root_dir = '/home/rakib/public_html/demo/'
REPO_URL = 'https://github.com/rakib-09/'+project_dir+'.git'


env.hosts = [
    '192.0.0.0:2222',  #your host server
]
# Set the username
env.user = "rakib"  #your username


def deploy():
    if exists(root_dir + project_dir):

        with cd(root_dir + project_dir):
            run('git fetch')
    else:
        with cd(root_dir):
            run(f'git clone {REPO_URL}')


def deploy_with_info(project, root, repo):
    if exists(root + project):

        with cd(root_dir + project_dir):
            run('git fetch')
    else:
        with cd(root_dir):
            run(f'git clone {repo}')

