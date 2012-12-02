# -*- coding: utf8 -*-
from phystricks import *
def figureXUQaJjF():
    pspicts,fig = MultiplePictures("figureXUQaJjF",2)
    pspicts[0].mother.caption=u"Une décroissante"
    pspicts[1].mother.caption=u"Une croissante"

    for psp in pspicts:
        psp.dilatation_X(0.7)
        psp.dilatation_Y(0.7)

    x=var('x')
    f=phyFunction(-x-2).graph(-4,2)
    g=phyFunction(x-2).graph(-2,4)
    fun=[f,g]

    for i,psp in enumerate(pspicts):
        k=fun[i]
        B=k.get_point(0)
        B.put_mark(0.2,B.advised_mark_angle,"\( b\)",automatic_place=psp)
        
        x0=solve(k(x)==0,x)[0].rhs()
        A=k.get_point(x0)
        A.put_mark(0.2,A.advised_mark_angle,"\( -b/a\)",automatic_place=psp)
        
        psp.DrawGraphs(k,B,A)
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.no_figure()
    fig.write_the_file()
