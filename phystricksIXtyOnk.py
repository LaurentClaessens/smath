# -*- coding: utf8 -*-
from phystricks import *
def IXtyOnk():
    pspict,fig = SinglePicture("IXtyOnk")
    pspict.dilatation_X(40)
    pspict.dilatation_Y(70)

    x=var('x')
    f=phyFunction(-5*x**2+x).graph(0,0.2)

    v=f.get_tangent_vector(0).fix_visual_size(3,pspict=pspict)
    v.parameters.color="red"

    zz=f.inverse(0)
    A=Point(zz[0],0)
    B=Point(zz[1],0)
    measure=MeasureLength(  Segment(A,B),0  )
    measure.put_mark(0.2,-90,"\( l\)",pspict=pspict)

    angle=AngleAOB( A,B,v.F   )
    angle.parameters.color="green"
    angle.put_mark(0.2,None,"\( \\alpha\)",pspict=pspict)

    pspict.DrawGraphs(f,v,measure,angle)
    pspict.axes.no_graduation()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
