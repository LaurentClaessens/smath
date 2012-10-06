# -*- coding: utf8 -*-

# Cette figure n'est utilisée que pour l'image; pas pour à la figure.
from phystricks import *

def put_at(pspict,f,x):
    g=-f
    P=f.get_point(x)
    Q=g.get_point(x)
    seg=Segment(P,Q)
    seg.parameters.color="red"
    seg.parameters.style="dashed"
    pspict.DrawGraphs(seg,P,Q)

def PasFonctionYoQfSu():
    pspict,fig = SinglePicture("PasFonctionYoQfSu")
    pspict.dilatation(0.7)

    x=var('x')
    mx=-4
    Mx=3
    f=phyFunction(sqrt(x+4)).graph(mx,Mx)
    g=-f
    #g=phyFunction(-sqrt(x+4)).graph(mx,Mx)

    
    pspict.DrawGraphs(f,g)
    
    put_at(pspict,f,-2)
    put_at(pspict,f,1)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
