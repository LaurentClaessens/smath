# -*- coding: utf8 -*-
from phystricks import *
def QEMNooDcNLFy():
    pspict,fig = SinglePicture("QEMNooDcNLFy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(3,-2)
    D=Point(-1,-2)

    O=C+(3,-1)

    Ap=A.symmetric_by(O)
    Bp=B.symmetric_by(O)
    Cp=C.symmetric_by(O)
    Dp=D.symmetric_by(O)

    original=Polygon(A,B,C,D)
    image=Polygon(Ap,Bp,Cp,Dp)

    original.put_mark(0.2,pspict=pspict)
    image.put_mark(0.2,text_list=["\( A'\)","\( B'\)","\( C'\)","\( D'\)"],pspict=pspict)

    O.parameters.symbol="*"
    O.put_mark(0.2,45,"\( O\)",automatic_place=(pspict,"corner"))

    seg1=Segment(B,Bp)
    seg1.divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)
    seg2=Segment(C,Cp)
    seg2.divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)


    pspict.DrawGraphs(original,image,O,seg1,seg2)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
