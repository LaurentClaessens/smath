#! /usr/bin/python3
# -*- coding: utf8 -*-

import sys
import shutil

filename=sys.argv[1]
other=filename+".tmp"

print(filename)

f1 = open(filename, 'r')
f2 = open(other, 'w')
for line in f1:
    newline=line
    newline=newline.replace('automatic_place=(pspicts,"center")','pspict=pspicts,position="center"')
    newline=newline.replace('automatic_place=(pspict,"center")','pspict=pspict,position="center"')
    f2.write(newline)
f1.close()
f2.close()

shutil.copy(other,filename)

if False:
    newline=newline.replace('automatic_place=pspict','pspict=pspict')
    newline=newline.replace('automatic_place=(pspicts,"")','pspict=pspicts')
    newline=newline.replace('automatic_place=(pspicts,"corner")','pspict=pspicts,position="corner"')
    newline=newline.replace('automatic_place=(pspicts,"N")','pspict=pspicts,position="N"')
    newline=newline.replace('automatic_place=(pspicts,"S")','pspict=pspicts,position="S"')
    newline=newline.replace('automatic_place=(pspicts,"E")','pspict=pspicts,position="E"')
    newline=newline.replace('automatic_place=(pspicts,"W")','pspict=pspicts,position="W"')
    newline=newline.replace('automatic_place=(pspicts,"")','pspict=pspicts')
    newline=newline.replace('automatic_place=(pspict,"corner")','pspict=pspict,position="corner"')
    newline=newline.replace('automatic_place=(pspict[1],"S")','pspict=pspict[1],position="S"')
    newline=newline.replace('automatic_place=(pspict[1],"E")','pspict=pspict[1],position="E"')
    newline=newline.replace('automatic_place=(pspict[1],"N")','pspict=pspict[1],position="N"')
    newline=newline.replace('automatic_place=(pspict[1],"W")','pspict=pspict[1],position="W"')
    newline=newline.replace('automatic_place=(pspict,"")','pspict=pspict')
    newline=newline.replace('automatic_place=(pspict,"N")','pspict=pspict,position="N"')
    newline=newline.replace('automatic_place=(pspict,"S")','pspict=pspict,position="S"')
    newline=newline.replace('automatic_place=(pspict,"E")','pspict=pspict,position="E"')
    newline=newline.replace('automatic_place=(pspict,"W")','pspict=pspict,position="W"')
