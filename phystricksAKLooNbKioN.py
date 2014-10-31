# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y):
    return Rectangle(  Point(x,y+1),Point(x+1,y) )

dilat=0.4

def SESooBTZQPF():
    pspict,fig = SinglePicture("SESooBTZQPF")
    pspict.dilatation(dilat)

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

def NNZooNCAqUK():
    pspict,fig = SinglePicture("NNZooNCAqUK")
    pspict.dilatation(dilat)

    for i in range(0,2):
        for j in range(0,3):
            pspict.DrawGraph(petit(i,j))
    for j in range(0,3):
        pet=petit(0,j)
        pet.parameters.hatched()
        pet.parameters.hatch.color='gray'
        pspict.DrawGraph(pet)
    for j in range(0,2):
        pet=petit(1,j)
        pet.parameters.filled()
        pet.parameters.fill.color='lightgray'
        pspict.DrawGraph(pet)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def CEZooPzIzzi():
    pspict,fig = SinglePicture("CEZooPzIzzi")
    pspict.dilatation(dilat)

    for i in range(0,5):
        for j in range(0,3):
            pspict.DrawGraph(petit(i,j))
    for j in range(1,3):
        for i in range(0,5):
            pet=petit(i,j)
            pet.parameters.hatched()
            pet.parameters.hatch.color='gray'
            pspict.DrawGraph(pet)
    pet=petit(0,0)
    pet.parameters.filled()
    pet.parameters.fill.color='lightgray'
    pspict.DrawGraph(pet)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


def AKLooNbKioN():
    SESooBTZQPF()
    NNZooNCAqUK()
    CEZooPzIzzi()
