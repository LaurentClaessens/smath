#! /usr/bin/env python3
# -*- coding: utf8 -*-

"""
Ce petit script m'a aidé à trouver les exercices includ plusieurs fois, et plus généralement les "blabla multiply defined"
Novembre 2016
"""

import os

def exo_files():
    for f in os.listdir("."):
        if f.startswith("exo") and f.endswith(".tex"):
            yield f.replace(".tex","")

def multiply_line(filename):
    with open(filename,'r') as f :
        for line in f.readlines():
            if "multiply" in line :
                yield line



duplicates=[]
with open('multiply.txt','r') as travail :
    for f in travail.readlines():
        duplicates.append(f[:-1])

a=[]
for f in exo_files():
    if f not in duplicates :
        print(r"\Exo{"+f[3:]+"}")
    else :
        a.append(f)

#for l in multiply_line("travail.txt"):
#    print(l[:-1])
print(len(a))
