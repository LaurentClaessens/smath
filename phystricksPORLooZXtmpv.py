# -*- coding: utf8 -*-
from phystricks import *
def PORLooZXtmpv():
    pspict,fig = SinglePicture("PORLooZXtmpv")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(3,1)
    C=Point(4,3)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,pspict=pspict)

    s1=Segment(A,B)
    s2=Segment(B,C)

    #A.put_mark(0.2,angle=None,text="\( A\)",automatic_place=(pspict,""))
    #B.put_mark(0.2,angle=None,text="\( B\)",automatic_place=(pspict,""))
    #C.put_mark(0.2,angle=None,text="\( C\)",automatic_place=(pspict,""))

    pspict.math_BB.append( Point(4,3),pspict )
    pspict.math_BB.append( Point(0,0),pspict )

    no_symbol(parall.vertices)

    pspict.comment="The grid is exactly one more than the points"
    pspict.DrawGraphs(s1,s2,parall.vertices[:-1])
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
