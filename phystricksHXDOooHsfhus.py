# -*- coding: utf8 -*-
from phystricks import *
def HXDOooHsfhus():
    pspict,fig = SinglePicture("HXDOooHsfhus")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    pr1=0.4
    pr2=0.7
    O=Point(0,0)
    P=Point(-2.5,3)
    Q=Point(3,3)
    A=Segment(O,P).get_point_proportion(pr1)
    B=Segment(O,P).get_point_proportion(pr2)
    C=Segment(O,Q).get_point_proportion(pr2)
    D=Segment(O,Q).get_point_proportion(pr1)
    
    p1=Segment(B,C).dilatation(1.3)
    p2=Segment(A,D).dilatation(2.1)
    d1=Segment(O,P)
    d2=Segment(O,Q)

    O.put_mark(0.1,angle=-45,text="\( O\)",automatic_place=(pspict,""))

    a1=Angle(C,B,P,r=0.3)
    a1.put_mark(0.2,angle=None,text="\SI{100}{\degree}",automatic_place=(pspict,""))
    a2=Angle(p2.F,D,Q)
    a2.put_mark(0.3,angle=None,text="\SI{30}{\degree}",automatic_place=(pspict,""))

    no_symbol(O)

    pspict.DrawGraphs(O,d1,d2,p1,p2,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
