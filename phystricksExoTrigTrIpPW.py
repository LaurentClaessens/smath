# -*- coding: utf8 -*-
from phystricks import *
def ExoTrigTrIpPW():
    pspict,fig = SinglePicture("ExoTrigTrIpPW")
    pspict.dilatation(1)

    A=Point(-2,1)
    B=Point(2,-1)
    x=var('x')
    f=phyFunction(2*x).graph(-2,2.5)
    f.parameters.color="black"
    C=f.get_point(1.7)
    AB=Segment(A,B).dilatation(1.5)
    AC=Segment(A,C).dilatation(1.5)
    CB=Segment(C,B).dilatation(1.5)


    AC.parameters.style="dashed"
    AC.parameters.color="blue"
    CB.parameters.style="dashed"
    CB.parameters.color="blue"
    
    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-20,"\( C\)",pspict=pspict)


    pspict.DrawGraphs(A,B,C,f,AB,AC,CB)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
