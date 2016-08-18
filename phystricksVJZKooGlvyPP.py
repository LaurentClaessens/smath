# -*- coding: utf8 -*-
from phystricks import *
def VJZKooGlvyPP():
    pspict,fig = SinglePicture("VJZKooGlvyPP")
    pspict.dilatation_Y(0.2)

    pts=[  Point(1,4),Point(2,8),Point(3,12),Point(4,16) ]
    pspict.DrawGraphs(pts)

    pspict.axes.single_axeX.put_mark(0.2,-45,"\SI{c}{\centi\meter} ",pspict=pspict,position="corner")
    pspict.axes.single_axeY.put_mark(0.2,-45,"\( p\)(\si{\centi\meter})",pspict=pspict,position="corner")
    pspict.axes.single_axeY.Dx=4
    
    seg=Segment( pts[0],pts[-1] ).dilatation(1.5)
    seg.parameters.style="dashed"

    pspict.DrawGraphs(seg)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
