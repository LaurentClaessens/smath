#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *
import random
import sys

n=100   # Ce nombre est dans phystricksSimulBinNWxfTN

def une_simulation(verbatim=True):
    P=0
    F=0
    for i in range(0,n):
        a=random.choice(["P","F"])
        if verbatim :
            print a,
        if a == "F":
            F=F+1
        if a == "P":
            P=P+1
    if verbatim:
        print "\n total :",F,"F et ",P,"P"
    return P

def plein_de_simulations(nombre=1000,montrer=True):
    resultats={  i:0 for i in range(0,n+1)  }
    if montrer :
        print resultats
    for i in range(0,nombre):
        P=une_simulation(False)
        resultats[P]=resultats[P]+1

    if montrer :
        G=point((0,0))
        for i in range(0,n):
            G=G+line([(i,0),(i,resultats[i])])
            print i,resultats[i]
        show(G)
    return resultats

if __name__=="main":
    une_simulation()
    plein_de_simulations(nombre=int(sys.argv[1]))
