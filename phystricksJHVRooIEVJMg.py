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
    surf.put_mark(0.2,pspicts=pspicts)
    surf.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\SI{6.28}{\centi\meter}",pspicts=pspicts)
    surf.edges[1].put_mark(0.2,angle=None,added_angle=180,text="\SI{3}{\centi\meter}",pspicts=pspicts)

    no_symbol(surf.vertices)

    i1=surf.edges[2].get_point_proportion(0.8)
    f1=i1+(0,2*rayon)
    base1=CircleAB(i1,f1)

    i2=surf.edges[0].get_point_proportion(0.8)
    f2=i2+(0,-2*rayon)
    base2=CircleAB(i2,f2)

    pspicts[0].DrawGraphs(base1)
    pspicts[1].DrawGraphs(base1,surf)
    pspicts[2].DrawGraphs(base1,surf,base2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

