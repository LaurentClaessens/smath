# -*- coding: utf8 -*-
from phystricks import *


def GLVooNqioTo():
    pspicts,figs = IndependentPictures("GLVooNqioTo",4)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    O=Point(0,0)
    r=1

    tartes=[]
    tartes.append(FractionPieDiagram(O,r,0,5))
    tartes.append(FractionPieDiagram(O,r,0,5))
    tartes.append(FractionPieDiagram(O,r,0,10))
    tartes.append(FractionPieDiagram(O,r,0,10))

    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(tartes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
