# -*- coding: utf8 -*-
from phystricks import *
def IUHooFrAHoa():
    pspict,fig = SinglePicture("IUHooFrAHoa")
    pspict.dilatation(1)

    A=Point(0,2)
    B=Point(-1,0)
    C=Point(0,-2)
    D=Point(1,0)

    loz=Polygon(A,B,C,D)
    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="S")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="E")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="N")
    D.put_mark(0.2,text="\( D\)",pspict=pspict,position="W")

    for seg in loz.edges:
        seg.put_code(n=3,l=0.2,d=0.1,pspict=pspict)

    pspict.DrawGraphs(loz,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
