#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# smath project.
#

import sys
from TestRecall import wrong_file_list

directory=sys.argv[1]

mfl,wfl=wrong_file_list(directory)

for f in mfl:
    print("missing recall : ",f)
for f in wfl:
    print("Wrong : ",f)

