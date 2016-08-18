# -*- coding: utf8 -*-
from phystricks import *
def UPGooXSYGqo():
    pspict,fig = SinglePicture("UPGooXSYGqo")
    pspict.dilatation(0.7)

    A=Point(0,0)
    D=Point(6,0)
    B=Point(1,3)
    C=Point(5,3)

    quadri=Polygon(A,B,C,D)
    diags=[Segment(A,C),Segment(B,D)]

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90+45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,-45,"\( D\)",pspict=pspict,position="corner")

    for d in diags:
        d.parameters.color="blue"

    pspict.DrawGraphs(A,B,C,D,quadri,diags)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
