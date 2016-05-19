# -*- coding: utf8 -*-
from phystricks import *
def TQDooEgJgPZ():
    x=var('x')
    F=[]
    F.append( phyFunction((x-1)/(x+1)).graph(-2.5,2.5) )
    F.append( phyFunction(1/x).graph(-3,3) )
    F.append( phyFunction(   x/(x+1)   ).graph(-2.5,2.5) )
    F.append( phyFunction(   (x+2)/(x-3)  ).graph(-3,8) )
    F.append( phyFunction( (x-3)/(x+4) ).graph(-8,4) )

    for f in F:
        f.cut_y(-5,5)

    pspicts,fig = MultiplePictures("TQDooEgJgPZ",len(F))
    for psp in pspicts:
        psp.dilatation_X(0.7)
        psp.dilatation_Y(0.7)

    for i in range(0,len(F)):
        pspicts[i].mother.caption="La fonction $"+latex(F[i].sage)+"$"

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(F[i])
        psp.axes.do_my_enlarge=False
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
