# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

from communPhys import Secteur
from communPhys import lignes

def IIHooSeavps():
    pspictA,figA = SinglePicture("DLPooHXskUP")
    pspictB,figB = SinglePicture("KRFooUgRQSB")
    pspictC,figC = SinglePicture("GFYooZOvPjP")

    pspicts=[pspictA,pspictB,pspictC]
    figs=[figA,figB,figC]
    
    for pspict in pspicts :
        pspict.dilatation_X(1)
        pspict.dilatation_Y(1)

    O=Point(0,0)
    cercle=Circle(O,1)

    secteurs=[]
    leslignes=[]
    secteurs.append(Secteur(cercle,0,360/3))
    leslignes.append(  lignes(3)  )

    secteurs.append(Secteur(cercle,0,3*360/5))
    leslignes.append(  lignes(5)  )

    secteurs.append(Secteur(cercle,0,3*360/4))
    leslignes.append(  lignes(4)  )

    for sect in secteurs :
        sect.parameters.filled()
        sect.parameters.fill.color="lightgray"
        #sect.draw_edges()
        #sect.edges.color="red"

    for i,psp in enumerate(pspicts) :
        psp.DrawGraphs(cercle,secteurs[i])
        psp.DrawGraphs(leslignes[i])
    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
