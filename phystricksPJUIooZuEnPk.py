# -*- coding: utf8 -*-

from phystricks import *

from communPhys import Secteur
from communPhys import lignes

def PJUIooZuEnPk():
    pspicts,figs = IndependentPictures("PJUIooZuEnPk",2)
    for psp in pspicts:
        psp.dilatation(1)

    O=Point(0,0)
    cercle=Circle(O,1)

    secteurs=[]
    leslignes=[]
    secteurs.append(Secteur(cercle,0,3*360/4))
    leslignes.append(  lignes(4)  )

    secteurs.append(Secteur(cercle,0,4*360/8))
    leslignes.append(  lignes(8)  )

    secteurs[0].parameters.filled()
    secteurs[0].parameters.fill.color="lightgray"

    for i,psp in enumerate(pspicts) :
        psp.DrawGraphs(cercle,secteurs[i])
        psp.DrawGraphs(leslignes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

