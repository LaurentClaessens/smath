# -*- coding: utf8 -*-
from phystricks import *
def QCARooMunXfF():
    pspict,fig = SinglePicture("QCARooMunXfF")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    B=O+(-2,-1)
    C=O+O-B
    cer=CircleOA(O,B)
    A=cer.get_point(90)
    cer.parameters.style="dashed"

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    O.put_mark(0.2,angle=-90,added_angle=0,text="\( O\)",automatic_place=(pspict,""))

    rh=RightAngleAOB(B,A,C,r=0.3,n1=0,n2=1)
    trig.edges[1].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspict)

    AO=Segment(A,O)
    AO.put_code(n=2,d=0.1,l=0.2,pspict=pspict)


    no_symbol(trig.vertices)

    pspict.comment="The circle is dashed"
    pspict.DrawGraphs(O,trig,cer,rh,AO)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
