# -*- coding: utf8 -*-
from phystricks import *
def QEMNooDcNLFy():
    pspict,fig = SinglePicture("QEMNooDcNLFy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(3,-2)
    D=Point(-1,-2)
    E=D+(1,-1)
    F=E+(1,1)

    O=C+(1,-1)

    Ap=A.symmetric_by(O)
    Bp=B.symmetric_by(O)
    Cp=C.symmetric_by(O)
    Dp=D.symmetric_by(O)
    Ep=E.symmetric_by(O)
    Fp=F.symmetric_by(O)

    original=Polygon(A,B,C,D)
    s1=Segment(D,E)
    s2=Segment(E,F)
    image=Polygon(Ap,Bp,Cp,Dp)
    s1p=Segment(Dp,Ep)
    s2p=Segment(Ep,Fp)


    original.put_mark(0.2,pspict=pspict)
    image.put_mark(0.2,text_list=["\( A'\)","\( B'\)","\( C'\)","\( D'\)"],pspict=pspict)

    O.parameters.symbol="*"
    O.put_mark(0.2,45,"\( O\)",pspict=pspict,position="corner")

    seg1=Segment(B,Bp)
    seg1.divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)
    seg2=Segment(C,Cp)
    seg2.divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)


    pspict.DrawGraphs(original,s1,s2,s1p,s2p,image,O,seg1,seg2)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
