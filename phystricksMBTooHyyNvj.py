# -*- coding: utf8 -*-
from phystricks import *
def MBTooHyyNvj():
    pspicts,figs = IndependentPictures("MBTooHyyNvj",3)

    for psp in pspicts:
        psp.dilatation(0.7)

    O=Point(0,0)
    r=1

    tartes=[]
    tartes.append(FractionPieDiagram(O,r,2,8))
    tartes.append(FractionPieDiagram(O,r,1,4))
    tartes.append(FractionPieDiagram(O,r,1,6))

    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(tartes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
