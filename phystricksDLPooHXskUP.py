# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from communPhys import Secteur,lignes

def DLPooHXskUP():
    pspict,fig = SinglePicture("DLPooHXskUP")

    O=Point(0,0)
    cercle=Circle(O,1)

    secteur=Secteur(cercle,0,360/3)
    ligne=  lignes(3)  
    secteur.parameters.filled()
    secteur.parameters.fill.color="lightgray"

    pspict.DrawGraphs(cercle,secteur,ligne)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
