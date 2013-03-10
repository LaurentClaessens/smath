# -*- coding: utf8 -*-
from phystricks import *
def ZCumAwy():
    pspict,fig = SinglePicture("ZCumAwy")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(2.5)

    x=var('x')
    mx=-10
    Mx=-mx
    f=phyFunction(1/x).graph(mx,Mx)
    f.cut_y(-1.2,1.2)

    b=-0.3
    B=Point(0,b)
    x0=f.inverse(b)[0]
    X=Point(x0,0)
    A=f.get_point(x0)
    l1=Segment(X,A)
    l2=Segment(A,B)
    l1.parameters.color="red"
    l1.parameters.style="dashed"
    l2.parameters.color="red"
    l2.parameters.style="dashed"

    B.put_mark(0.2,0,"\( -1/10\)",automatic_place=pspict)
    X.put_mark(0.2,90,"\( -10\)",automatic_place=pspict)

    w1=Segment( Point(mx,0),Point(x0,0)  )
    w1.parameters.color="green"
    w1.wave(0.4,0.05)

    w2=Segment( Point(0,0),Point(Mx,0)  )
    w2.parameters.color="green"
    w2.wave(0.4,0.05)

    pspict.DrawGraphs(f,A,B,X,l1,l2,w1,w2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
