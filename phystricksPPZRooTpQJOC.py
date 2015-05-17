# -*- coding: utf8 -*-
from phystricks import *

from phystricksCommons import Pyramide

def PPZRooTpQJOC():
    pspicts,figs = IndependentPictures("PPZRooTpQJOC",2)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( -2\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( 5\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -2\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( -1\)",automatic_place=(pspicts,"center"))
    pspicts[0].DrawGraphs(pyramide)

    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,3)].put_mark(0.0,0,"\( -1.7\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(0,2)].put_mark(0.0,0,"\( -4.5\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(1,1)].put_mark(0.0,0,"\( 2.1\)",automatic_place=(pspicts,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\(1.2\)",automatic_place=(pspicts,"center"))
    pspicts[1].DrawGraphs(pyramide)



    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
