# -*- coding: utf8 -*-
from phystricks import *
def PATooDkWFPD():
    pspicts,figs = IndependentPictures("PATooDkWFPD",2)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    O=Point(0,0)
    r=1

    tarte1=FractionPieDiagram(O,r,2,8)
    tarte2=FractionPieDiagram(O,r,1,4)

    pspicts[0].DrawGraphs(tarte1)
    pspicts[1].DrawGraphs(tarte2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
