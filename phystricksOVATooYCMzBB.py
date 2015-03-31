# -*- coding: utf8 -*-
from phystricks import *
def OVATooYCMzBB():
    pspict,fig = SinglePicture("OVATooYCMzBB")
    pspict.dilatation(1)

    B=Point(0,0)
    cer=Circle(B,3)
    C=cer.get_point(-40)
    A=cer.get_point(-90)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    #aA=Angle(C,A,B)
    aB=Angle(A,B,C,r=0.3)
    #aC=Angle(B,C,A,r=0.3)

    aB.put_mark(0.3,angle=None,added_angle=0,text="\SI{40}{\degree}",automatic_place=(pspict,""))
    trig.edges[0].put_code(n=2,d=0.1,l=0.3,pspict=pspict)
    trig.edges[1].put_code(n=2,d=0.1,l=0.3,pspict=pspict)

    no_symbol(A,B,C)

    pspict.DrawGraphs(trig,aB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
