# -*- coding: utf8 -*-
from phystricks import *
def ExVarGraphiqueyhHpqn():
    pspicts,fig = MultiplePictures("ExVarGraphique",3,script_filename="ExVarGraphiqueyhHpqn")
    pspicts[0].mother.caption="Une fonction"
    pspicts[1].mother.caption="Une fonction"
    pspicts[2].mother.caption="Une fonction"

    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    x=var('x')
    f=[]
    f.append( phyFunction((x+2)**2).graph(-4,0) )
    f.append( HermiteInterpolation( [(-3,0,-1),(-2,-1,0),(0,2,0),(1,0,0)] ).graph(-3,1.3)  )
    f.append( HermiteInterpolation([(-4,-2,0),(-1,1,0),(2,-1,0)]).graph(-4.5,3) )

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(f[i])
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()

