# -*- coding: utf8 -*-
from phystricks import *
def SESooBTZQPF():
    from communPhys import petitAKL
    dilat=0.4
    pspict,fig = SinglePicture("SESooBTZQPF")
    pspict.dilatation(dilat)

    for i in range(0,4):
        for j in range(0,3):
            pspict.DrawGraphs(petitAKL(i,j))
    for i in range(0,4):
        pet=petitAKL(i,0)
        pet.hatched()
        pet.hatch_parameters.color='gray'
        pspict.DrawGraphs(pet)
    for i in range(0,4):
        pet=petitAKL(i,1)
        pet.filled()
        pet.fill_parameters.color='lightgray'
        pspict.DrawGraphs(pet)
    for i in range(0,3):
        pet=petitAKL(i,2)
        pet.filled()
        pet.fill_parameters.color='lightgray'
        pspict.DrawGraphs(pet)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

