# -*- coding: utf8 -*-
from phystricks import *
def TWGooMalxLa():
    pspicts,fig = MultiplePictures("TWGooMalxLa",3)
    pspicts[0].mother.caption="Un graphe"
    pspicts[1].mother.caption="Un autre"
    pspicts[2].mother.caption="Et un dernier"

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.1)

    x=var('x')
    F=[]
    F.append( phyFunction(x**2+3*x-10).graph(-10,10) )
    F.append( phyFunction(-x**2-3*x+10).graph(-10,10) )
    F.append( phyFunction( (x-2)*(x+4.5)  ).graph(-10,10) )

    for f in F:
        f.cut_y(-20,20)
    
    for i in range(0,len(pspicts)):
        pspicts[i].DrawGraphs(F[i])

    for psp in pspicts:
        psp.axes.single_axeX.Dx=2
        psp.axes.single_axeY.Dx=10
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
