# -*- coding: utf8 -*-
from phystricks import *
def FnAffineipcEQf():
    pspicts,fig = MultiplePictures("FnAffineipcEQf",2)
    pspicts[0].mother.caption="\( m>0\)"
    pspicts[1].mother.caption="\( m<0\)"

    for psp in pspicts:
        psp.dilatation_Y(0.7)
        psp.dilatation_X(0.7)

    x=var('x')
    f=[]
    f.append( phyFunction(x/1.5+2).graph(-4,2) )
    f.append( phyFunction(-3*x/2+1).graph(-2,2) )

    for i,psp in enumerate(pspicts):
        P=Point(f[i].inverse(0)[0],0)
        P.put_mark(0.2,text="\( -\\frac{ p }{ m }\)",pspict=psp,position="N")
        P.parameters.symbol="|"

        Q=f[i].get_point(0)
        Q.put_mark(0.2,180,"\( p\)",pspict=psp)
        Q.parameters.symbol="|"
        Q.add_option("dotangle=90")

        psp.axes.no_graduation()
        psp.DrawGraphs(f[i],P,Q)
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

