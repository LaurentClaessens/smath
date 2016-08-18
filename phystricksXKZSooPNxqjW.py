# -*- coding: utf8 -*-
from phystricks import *
def XKZSooPNxqjW():
    pspict,fig = SinglePicture("XKZSooPNxqjW")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    mx=-5
    Mx=5
    O=Point(0,0)

    A=Point(3,0)
    B=Point(-3,0)
    C=Point(4,0)
    D=Point(-0.75,0)
    E=Point(-4,0)

    A.put_mark(0.2,angle=90,added_angle=0,text="\( A\)",pspict=pspict)
    B.put_mark(0.2,angle=90,added_angle=0,text="\( B\)",pspict=pspict)
    C.put_mark(0.2,angle=90,added_angle=0,text="\( C\)",pspict=pspict)
    D.put_mark(0.2,angle=90,added_angle=0,text="\( D\)",pspict=pspict)
    E.put_mark(0.2,angle=90,added_angle=0,text="\( E\)",pspict=pspict)

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    #axe.no_numbering()

    pspict.DrawGraphs(axe,A,B,C,D,E)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
