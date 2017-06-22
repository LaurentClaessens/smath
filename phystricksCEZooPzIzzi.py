# -*- coding: utf8 -*-
from phystricks import *
def CEZooPzIzzi():
    from communPhys import petitAKL
    dilat=0.4
    pspict,fig = SinglePicture("CEZooPzIzzi")
    pspict.dilatation(dilat)

    for i in range(0,5):
        for j in range(0,3):
            pspict.DrawGraphs(petitAKL(i,j))
    for j in range(1,3):
        for i in range(0,5):
            pet=petitAKL(i,j)
            pet.hatched()
            pet.hatch_parameters.color='gray'
            pspict.DrawGraphs(pet)
    pet=petitAKL(0,0)
    pet.filled()
    pet.fill_parameterscolor='lightgray'
    pspict.DrawGraphs(pet)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
