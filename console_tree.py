#!/usr/bin/env python3
import os
import sys
import subprocess


class GitRepo:
    
    def __init__(self, repo_path, commit_count):
        self.repo_path = repo_path
        self.commit_count = commit_count
        # TODO: add repo statistic 
        # self.commit_count = .....
        
    def __str__(self):
        return f'Path: {self.repo_path} Commit count: {self.commit_count}'



root_dir = os.path.join(sys.argv[1])\
    if len(sys.argv) > 1 else \
    os.path.expanduser('~')

git_repos = list()
for root, dirs, files in os.walk(root_dir, topdown=True):
    if '.git' in dirs:
        dirs = []
        os.chdir(root)
        commit_count = subprocess.run(['git', 'rev-list', '--count', '--all'], stdout=subprocess.PIPE).stdout
        new_repo = GitRepo(os.path.abspath(root), int(commit_count.decode().strip()))
        git_repos.append(new_repo)



for i, git_repo in enumerate(git_repos):
    print(f'{i + 1}. {git_repo}')
