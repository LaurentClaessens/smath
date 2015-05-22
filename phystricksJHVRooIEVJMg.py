# -*- coding: utf8 -*-
from phystricks import *
def JHVRooIEVJMg():
    pspicts,figs = IndependentPictures("JHVRooIEVJMg",3)

    for psp in pspicts:
        psp.dilatation(1)

    rayon=1
    hauteur=3
    peri=2*pi*rayon
    A=Point(0,0)
    B=A+(peri,0)
    C=B+(0,hauteur)
    D=A+C-B

    surf=Polygon(A,B,C,D)
    surf.put_mark(0.2,pspict=pspicts)
    surf.edges[0].put_mark(-0.2,angle=None,added_angle=0,text="\SI{6.28}{\centi\meter}",automatic_place=(pspicts,""))
    surf.edges[1].put_mark(-0.2,angle=None,added_angle=0,text="\SI{3}{\centi\meter}",automatic_place=(pspicts,""))

    for psp in pspicts:
        psp.DrawGraphs(surf)

    i1=sef.edges[2].get_point_proportion(0.7)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

