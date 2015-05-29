# -*- coding: utf8 -*-
from phystricks import *
def LCUooNGZJFk():
    pspict,fig = SinglePicture("LCUooNGZJFk")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    A=Point(0,0)
    l=4
    h=2
    B=A+(l,0)
    C=B+(0,h)
    D=C+(-l,0)
    rect=Polygon(A,B,C,D)

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,90+45,"\( D\)",automatic_place=(pspict,"corner"))

    for P in [A,B,C,D]:
        P.parameters.symbol=""

    measureDC=MeasureLength(  Segment(D,C),-0.3  )
    measureDC.put_mark(0.3,90,"\SI{5}{\centi\meter}",automatic_place=(pspict,"S"))

    measureDA=MeasureLength(  Segment(D,A),0.3  )
    measureDA.put_mark(0.3,180,"\( h\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(rect,A,B,C,D,measureDC,measureDA)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
