# -*- coding: utf8 -*-
from phystricks import *
def DPXooCqCUDl():

    pspicts,fig = MultiplePictures("DPXooCqCUDl",2)
    pspicts[0].mother.caption="D'abord trouver quelque points de la droite"
    pspicts[1].mother.caption="et ensuite tracer."

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    x=var('x')
    f=phyFunction(2*x+1).graph(-3,2)

    for x in [-2,-1,0,1,1.5]:
        P=f.get_point(x)
        for psp in pspicts:
            psp.DrawGraphs(P)

    pspicts[1].DrawGraphs(f)

    for psp in pspicts:
        psp.DrawDefaultGrid()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
