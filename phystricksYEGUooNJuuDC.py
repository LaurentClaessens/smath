# -*- coding: utf8 -*-
from phystricks import *
def YEGUooNJuuDC():
    pspict,fig = SinglePicture("YEGUooNJuuDC")
    pspict.dilatation(0.7)

    F=Point(0,4)
    C=Point(4,4)
    B=Point(4,0)
    A=Point(0,0)
    E=Point(0,6)
    D=Point(2,4)

    O=Point(10,5)
    O.put_mark(0.2,-45,"\( O\)",automatic_place=(pspict,""))

    poly=Polygon(A,B,C,D,E,F)
    poly.put_mark(0.3,pspict=pspict)
    seg=Segment(D,F)

    F.mark.angle=180
    F.mark.automatic_place=(pspict,"E")

    pts=[A,B,C,D,E,F]
    for p in pts:
        p.parameters.symbol=""
    syms=[x.symmetric_by(O) for x in pts]
    S=Point( max(  [p.x for p in syms]  ),max( [p.y for p in syms] ) )
    S.parameters.symbol="\hphantom{A}"
    S.parameters.symbol=" "

    pspict.comment="La marque du 'F' est correctement placée à l'extérieur du polygone. \n Et la figure prend assez de place pour mettre le symétrique par rapport à O. Il y a donc du blanc au-dessus et le dessin arrive assez bien à gauche."
    pspict.DrawGraphs(poly,seg,O,S)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
