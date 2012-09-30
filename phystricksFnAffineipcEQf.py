# -*- coding: utf8 -*-
from phystricks import *
def FnAffineipcEQf():
    pspicts,fig = MultiplePictures("FnAffineipcEQf",2)
    pspicts[0].mother.caption="\( a>0\)"
    pspicts[1].mother.caption="\( a<0\)"

    for psp in pspicts:
        psp.dilatation_Y(0.7)
        psp.dilatation_X(0.7)

    x=var('x')
    f=[]
    f.append( phyFunction(x/2+1).graph(1,5) )
    f.append( phyFunction(-3*x/2+1).graph(0,5) )

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(f[i])
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()

