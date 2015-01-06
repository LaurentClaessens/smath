# -*- coding: utf8 -*-
from phystricks import *
def LZKGooYGQxGy():
    pspict,fig = SinglePicture("LZKGooYGQxGy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    H=Point(0,0)
    T=Point(-1,-4)*0.6
    E=Point(1.7,-4)*0.6

    s1=Segment(H,T).dilatation(1.2)
    s2=Segment(H,E).dilatation(1.2)

    O=Segment(H,T).get_point_proportion(0.3)
    L=Segment(H,E).get_point_proportion(0.3)
    p1=Segment(T,E).dilatation(1.2)
    p2=Segment(O,L).dilatation(1.6)

    H.put_mark(0.2,0,"\( H\)",automatic_place=(pspict,"W"))
    O.put_mark(0.2,90+45,"\( O\)",automatic_place=(pspict,"corner"))
    L.put_mark(0.2,45,"\( L\)",automatic_place=(pspict,"corner"))
    T.put_mark(0.2,-45,"\( T\)",automatic_place=(pspict,"corner"))
    E.put_mark(0.2,-45,"\( E\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(s1,s2,p1,p2,H,O,L,T,E)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
