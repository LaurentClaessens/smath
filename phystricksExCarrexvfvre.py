# -*- coding: utf8 -*-

from phystricks import *
def ExCarrexvfvre():
    pspict,fig = SinglePicture("ExCarrexvfvre")
    pspict.dilatation_Y(0.7)

    mx=-2.5
    Mx=2.5

    x=var('x')
    a=4
    f=phyFunction(x**2).graph(mx,Mx)
    absisses=f.inverse(a)

    for x in absisses :
        P=f.get_point(x)
        Q=Point(x,0)
        seg=Segment(P,Q)
        seg.parameters.color="red"
        seg.parameters.style="dotted"
        seg.put_arrow(size=0.1)
        pspict.DrawGraphs(seg,P)

    g=phyFunction(a).graph(mx,Mx)
    g.parameters.color="cyan"
    g.parameters.style="dashed"

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
