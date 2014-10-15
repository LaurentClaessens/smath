# -*- coding: utf8 -*-
from phystricks import *
def RBEooLYHhMX():
    pspicts,figs = IndependentPictures("RBEooLYHhMX",3)
    for psp in pspicts:
        psp.dilatation(1)

    tartes=[]
    tartes.append(FractionPieDiagram(Point(0,0),1,2,3))
    tartes.append(FractionPieDiagram(Point(0,0),1,4,4))
    tartes.append(FractionPieDiagram(Point(0,0),1,1,4))

    for i in range(0,3):
        pspicts[i].DrawGraphs(tartes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

