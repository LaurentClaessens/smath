# -*- coding: utf8 -*-
from phystricks import *
def GLVooUSQccD():
    pspicts,figs = IndependentPictures("GLVooUSQccD",2)

    r=1
    O=Point(0,0)
    tartes=[]
    tartes.append(FractionPieDiagram(O,r,1,2))
    tartes.append(FractionPieDiagram(O,r,1,1))

    for psp in pspicts :
        psp.dilatation(1)

    pspicts[0].DrawGraphs(tartes[0])
    pspicts[1].DrawGraphs(tartes[1])

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
