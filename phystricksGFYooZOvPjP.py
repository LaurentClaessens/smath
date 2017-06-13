# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from communPhys import Secteur,lignes

def GFYooZOvPjP():
    pspict,fig = SinglePicture("GFYooZOvPjP")

    O=Point(0,0)
    cercle=Circle(O,1)

    secteur=Secteur(cercle,0,3*360/4)
    ligne=  lignes(4)
    secteur.parameters.filled()
    secteur.parameters.fill.color="lightgray"

    pspict.DrawGraphs(cercle,secteur,ligne)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

