# -*- coding: utf8 -*-
from phystricks import *
def XYXooNdhQer():
    pspicts,figs = IndependentPictures("XYXooNdhQer",3)

    for psp in pspicts:
        psp.dilatation(0.7)

    O=Point(0,0)
    r=1

    tartes=[]
    tartes.append(FractionPieDiagram(O,r,4,12))
    tartes.append(FractionPieDiagram(O,r,3,5))
    tartes.append(FractionPieDiagram(O,r,1,3))

    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(tartes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
