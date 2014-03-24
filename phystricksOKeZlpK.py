# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def OKeZlpK():
    pspict,fig = SinglePicture("OKeZlpK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')

    lin=phyFunction(2*x/3+1).graph(-3,4)
    P=lin.get_point(0)
    Q=lin.get_point(1.5)
    M=lin.get_point(3)

    P.put_mark(0.2,135,"\( p\)",automatic_place=(pspict,"corner"))
    P.parameters.symbol="|"
    P.add_option("dotangle=90")
    Q.put_mark(0.2,Q.advised_mark_angle,"\( Q\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,M.advised_mark_angle,"\( M\)",automatic_place=(pspict,"corner"))

    Qx=Q.projection(pspict.axes.single_axeX)
    Qy=Q.projection(pspict.axes.single_axeY)
    Mx=M.projection(pspict.axes.single_axeX)
    My=M.projection(pspict.axes.single_axeY)
    
    Qx.parameters.symbol="|"
    Qy.parameters.symbol="|"
    Mx.parameters.symbol="|"
    My.parameters.symbol="|"

    Qx.put_mark(0.2,-90,"\( 1\)",automatic_place=(pspict,"N"))
    Qy.put_mark(0.2,180,"\( q\)",automatic_place=(pspict,"E"))
    Mx.put_mark(0.2,-90,"\( x_M \)",automatic_place=(pspict,"N"))
    My.put_mark(0.2,180,"\( y_M\)",automatic_place=(pspict,"E"))

    Qy.add_option("dotangle=90")
    My.add_option("dotangle=90")

    s1=Segment(Q,Qx)
    s2=Segment(Q,Qy)
    s3=Segment(M,Mx)
    s4=Segment(M,My)

    s1.parameters.style="dotted"
    s2.parameters.style="dotted"
    s3.parameters.style="dotted"
    s4.parameters.style="dotted"

    S=Point(M.x,P.y)
    horiz=Segment(P,S)
    R=Point(Q.x,P.y)

    S.put_mark(0.2,-45,"\( S\)",automatic_place=(pspict,"corner"))
    R.put_mark(0.2,-45,"\( R\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(P,Q,M,lin,Qx,Qy,Mx,My,s1,s2,s3,s4,horiz,R,S)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

