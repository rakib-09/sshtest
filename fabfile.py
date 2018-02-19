import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

project_dir = 'sshtest'
root_dir = '/home/ab2603/public_html/demo/'
REPO_URL = 'https://github.com/rakib-09/'+project_dir+'.git'


env.hosts = [
    '192.185.2.62:2222',
]
# Set the username
env.user = "ab2603"


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


# def _get_latest_source():
#     if exists(Folder_name):
#         cd(Folder_name)
#         run('git fetch')
#     else:
#         run(f'git clone {REPO_URL}')
#     current_commit = local("git log -n 1 --format=%H", capture=False)
#     run(f'git reset --hard {current_commit}')
