from __future__ import print_function   
from collections import defaultdict
import hashlib
import os
import sys


lines_seen = set() 

with open("", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
