# -*- coding: utf8 -*-
from phystricks import *
def IXtyOnk():
    pspict,fig = SinglePicture("IXtyOnk")
    pspict.dilatation_X(40)
    pspict.dilatation_Y(70)

    x=var('x')
    f=phyFunction(-5*x**2+x).graph(0,0.2)

    v=f.get_tangent_vector(0).visual_length(3,pspict=pspict)
    v.parameters.color="red"

    zz=f.inverse(0)
    measure=MeasureLength(  Segment(Point(zz[0],0),Point(zz[1],0)),0  )
    measure.put_mark(0.2,-90,"\( l\)")

    pspict.DrawGraphs(f,v,measure)
    pspict.axes.no_graduation()
    #pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
