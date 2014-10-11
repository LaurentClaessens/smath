# -*- coding: utf8 -*-
from phystricks import *
def KUUooRcCjkQ():
    pspicts,figs = IndependentPictures("KUUooRcCjkQ",3)

    for psp in pspicts:
        psp.dilatation(1)

    O=Point(0,0)
    r=1

    tartes=[]
    tartes.append(FractionPieDiagram(O,r,4,7))
    tartes.append(FractionPieDiagram(O,r,4,28))
    tartes.append(FractionPieDiagram(O,r,1,7))

    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(tartes[i])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
