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
    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,180,"\( B\)",automatic_place=(pspict,"E"))
    C.put_mark(0.2,-90,"\( C\)",automatic_place=(pspict,"N"))
    D.put_mark(0.2,0,"\( D\)",automatic_place=(pspict,"W"))

    for seg in loz.edges:
        seg.put_code(n=3,l=0.2,d=0.1,pspict=pspict)

    pspict.DrawGraphs(loz,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
