# -*- coding: utf8 -*-
from phystricks import *
def IBmsroy():
    pspict,fig = SinglePicture("IBmsroy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=A+(5,0)
    C=B+(0,3)
    D=A+(0,6)

    quadri=Polygon(A,B,C,D)
    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,90+45,"\( D\)",automatic_place=(pspict,"corner"))

    measureAB=MeasureLength(Segment(A,B),0.2)
    measureAB.put_mark(0.3,-90,"\( 5\)",automatic_place=pspict)

    measureBC=MeasureLength(Segment(B,C),0.2)
    measureBC.put_mark(0.3,0,"\( 3\)",automatic_place=pspict)

    measureAD=MeasureLength(Segment(A,D),-0.2)
    measureAD.put_mark(0.3,180,"\( 6\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,D,quadri,measureAB,measureBC,measureAD)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
