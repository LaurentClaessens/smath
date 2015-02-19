# -*- coding: utf8 -*-
from phystricks import *
def SRYNooEdaMMH():
    pspict,fig = SinglePicture("SRYNooEdaMMH")
    pspict.dilatation(0.7)

    A=Point(2,1)
    B=A+(3,0)
    C=B+(0,1)
    D=A+(0,1)
    E=C+(-1,1)
    O=Point(0,0)

    seg=[   Segment(A,B),Segment(B,C),Segment(C,D),Segment(C,E),Segment(D,A)   ]
    segprime=[  x.symmetric_by(O) for x in seg  ]

    poly=Polygon( A,B,C,D  )
    poly.put_mark(0.2,points_names="ABCD",pspict=pspict)
    E.put_mark(0.1,angle=90,text="\( E\)",automatic_place=(pspict,""))
    O.put_mark(0.05,angle=90+45,text="\( O\)",automatic_place=(pspict,""))


    no_symbol(poly.vertices,E,O)

    #pspict.axes.single_axeX.Dx=2
    #pspict.axes.single_axeY.Dx=2

    for s in segprime:
        pspict.math_BB.append(s,pspict)
    pspict.DrawGraphs(poly,seg,E,O)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
