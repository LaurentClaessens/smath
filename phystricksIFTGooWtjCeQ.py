# -*- coding: utf8 -*-
from phystricks import *
def IFTGooWtjCeQ():
    pspict,fig = SinglePicture("IFTGooWtjCeQ")
    pspict.dilatation(0.3)

    F=Point(0,0)
    G=Point(6,0)
    H=Point(3.5,4)

    triangle=Polygon(F,G,H)
    M=triangle.edges[0].midpoint()
    s1=Segment(F,M)
    s2=Segment(M,G)
    s1.put_code(n=2,l=1,d=0.4,pspict=pspict)
    s2.put_code(n=2,l=1,d=0.4,pspict=pspict)

    for p in [F,G,H,M]:
        p.parameters.symbol=""

    triangle.edges[1].put_code(n=1,l=1,d=0.1,angle=-45,pspict=pspict)
    triangle.edges[2].put_code(n=1,l=1,d=0.1,angle=45,pspict=pspict)

    F.put_mark(0.2,180+45,"\( F\)",pspict=pspict,position="corner")
    G.put_mark(0.2,-45,"\( G\)",pspict=pspict,position="corner")
    H.put_mark(0.2,45,"\( H\)",pspict=pspict,position="corner")
    M.put_mark(0.2,-90,"\( M\)",pspict=pspict,position="N")

    haut=Segment(H,M)
    haut.parameters.style='dashed'

    pspict.DrawGraphs(triangle,s1,s2,F,G,H,M,haut)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
