#!/usr/bin/env python3

import os

os.system('git rev-list --all --count') 
for root, dirs, files in os.walk(".git/", topdown=False):
#    for name in files:
#        print(os.path.join(root))
    for name in dirs:
       print(os.path.join(root, name))
       
       