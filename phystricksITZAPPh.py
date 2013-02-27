# -*- coding: utf8 -*-
from phystricks import *
def ITZAPPh():
    pspicts,fig = MultiplePictures("ITZAPPh",4)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    x=var('x')
    F=[]
    F.append(  phyFunction(-x+1).graph(-3,4)  )
    F.append(  phyFunction(x+4).graph(-3,4)  )
    F.append(  phyFunction(x/2-1).graph(-3,4)  )
    F.append(  phyFunction(2*x-1).graph(-2,2)  )

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(F[i])

    for psp in pspicts:
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()
