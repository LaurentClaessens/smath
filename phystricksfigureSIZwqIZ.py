# -*- coding: utf8 -*-
from phystricks import *
def figureSIZwqIZ():
    pspicts,fig = MultiplePictures("figureSIZwqIZ",4)
    pspicts[0].mother.caption="Une fonction"
    pspicts[1].mother.caption="Une fonction"
    pspicts[2].mother.caption="Une fonction"
    pspicts[3].mother.caption="Une fonction"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(0.5)

    x=var('x')

    F=[]
    F.append(phyFunction(x**2).graph(-2.5,2.5))
    F.append(phyFunction( 1-x**2 ).graph(-2,2))
    F.append(phyFunction( x+1 ).graph(-2,3))
    F.append(phyFunction( (x+2)**2 ).graph(-4,0.5))

    for i,psp in enumerate(pspicts):
       psp.DrawGraph(F[i])

    for psp in pspicts:
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()
