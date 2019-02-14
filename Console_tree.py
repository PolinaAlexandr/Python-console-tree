#!/usr/bin/env python3

import os

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       os.system('git log')      
       print(os.path.join(root, name))
   for name in dirs:
       print(os.path.join(root, name))