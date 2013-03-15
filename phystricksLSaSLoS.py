# -*- coding: utf8 -*-
from phystricks import *
def LSaSLoS():
    x=var('x')
    F=[]
    F.append( phyFunction(x**2).graph(-2.5,2.5) )
    #F.append( phyFunction(x**2-x).graph(-2.5,3.5) )
    #F.append( phyFunction(x**2-x+3).graph(-2.5,3.5) )
    #F.append( phyFunction(-x**2+2*x+3).graph(-2.5,4.5) )
    #F.append( phyFunction( -(x-3)*(x+4) ).graph(-5,4) )

    pspicts,fig = MultiplePictures("LSaSLoS",len(F))

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    for i in range(0,len(F)):
        pspicts[i].mother.caption="La fonction $"+latex(F[i].sage)+"$"

    for i,psp in enumerate(pspicts):
        psp.DrawGraph(F[i])
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
