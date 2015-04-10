# -*- coding: utf8 -*-

from __future__ import unicode_literals
from phystricks import *

def QJGGooLkuRLI():
    pspict,fig = SinglePicture("QJGGooLkuRLI")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,2)
    C=Point(-3,4)

    A.put_mark(0.2,angle=-90,added_angle=0,text="Alice",automatic_place=(pspict,""))
    B.put_mark(0.2,angle=0,added_angle=0,text="Bob",automatic_place=(pspict,""))
    C.put_mark(0.2,angle=90+45,added_angle=0,text="Chloé",automatic_place=(pspict,""))

    xmin=min(  [ P.x for P in [A,B,C] ]  )
    xmax=max(  [ P.x for P in [A,B,C] ]  )
    ymin=min(  [ P.y for P in [A,B,C] ]  )
    ymax=max(  [ P.y for P in [A,B,C] ]  )
    pspict.math_BB.append(  Point(xmin-1,ymin-1),pspict   )
    pspict.math_BB.append(  Point(xmax+1,ymax+1),pspict   )

    pspict.DrawGraphs(A,B,C)
    fig.no_figure()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
