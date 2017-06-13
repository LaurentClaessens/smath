# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from communPhys import Secteur,lignes

def KRFooUgRQSB():
    pspict,fig = SinglePicture("KRFooUgRQSB")

    O=Point(0,0)
    cercle=Circle(O,1)

    secteur=Secteur(cercle,0,3*360/5)
    lignes=  lignes(5)  
    secteur.parameters.filled()
    secteur.parameters.fill.color="lightgray"

    pspict.DrawGraphs(cercle,secteur)
    pspict.DrawGraphs(lignes)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

