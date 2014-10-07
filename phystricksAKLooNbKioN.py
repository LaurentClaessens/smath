# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y):
    return Rectangle(  Point(x,y+1),Point(x+1,y) )

def AKLooNbKioN():
    pspict,fig = SinglePicture("AKLooNbKioN")
    pspict.dilatation(0.4)

    for i in range(0,4):
        for j in range(0,3):
            pspict.DrawGraph(petit(i,j))
    for i in range(0,4):
        pet=petit(i,0)
        pet.parameters.hatched()
        pet.parameters.hatch.color='gray'
        pspict.DrawGraph(pet)
    for i in range(0,4):
        pet=petit(i,1)
        pet.parameters.filled()
        pet.parameters.fill.color='lightgray'
        pspict.DrawGraph(pet)
    for i in range(0,3):
        pet=petit(i,2)
        pet.parameters.filled()
        pet.parameters.fill.color='lightgray'
        pspict.DrawGraph(pet)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
