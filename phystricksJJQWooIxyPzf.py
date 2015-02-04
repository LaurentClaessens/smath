# -*- coding: utf8 -*-
from phystricks import *
def JJQWooIxyPzf():
    pspict,fig = SinglePicture("JJQWooIxyPzf")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    s1=Segment(A,B).dilatation(1.3)
    C=A+(0,-1)
    s2=s1.parallel_trough(C)

    O=Point(2,-3)
    c1=Segment(O,A).dilatation(1.3)
    c2=Segment(O,B).dilatation(1.3)


    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,""))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,""))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,""))

    K=Intersection(s2,c1)[0]

    ang1=Angle(c2.F,B,A,r=0.3)
    ang2=Angle(A,K,C,r=0.3)
    ang1.put_mark(0.2,None,"\SI{110}{\degree}",automatic_place=(pspict,""))
    ang2.put_mark(0.2,None,"\SI{50}{\degree}",automatic_place=(pspict,""))

    pspict.DrawGraphs(s1,s2,c1,c2,ang1,ang2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
