#!/usr/bin/env python3
import os
import sys


class GitRepo:
    
    def __init__(self, repo_path):
        self.repo_path = repo_path

        # TODO: add repo statistic
        # self.commit_count = .....


# while True:
root_dir = os.path.join(sys.argv[1])\
    if len(sys.argv) > 1 else \
    os.path.expanduser('~')


git_repos = list()
# while True:
for root, dirs, files in os.walk(root_dir, topdown=True):
    dirs[:] = [ dir for dir in dirs if dir == '.git']
    new_repo = GitRepo(os.path.abspath(root))
    git_repos.append(new_repo)
        # break

for git_repo in git_repos:
    print(git_repo.repo_path)
