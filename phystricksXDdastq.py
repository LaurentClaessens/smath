# -*- coding: utf8 -*-
from phystricks import *
def XDdastq():
    pspict,fig = SinglePicture("XDdastq")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    I=Point(0,0)
    r2=3
    r1=1

    C1=Circle(  I,r1  )
    C2=Circle(  I,r2  )

    K=C2.get_point(0)
    C=C2.get_point(60)
    A=C2.get_point(120)
    G=C2.get_point(180)
    O=C2.get_point(240)
    Q=C2.get_point(300)

    J=C1.get_point(0)
    E=C1.get_point(60)
    D=C1.get_point(120)
    H=C1.get_point(180)
    L=C1.get_point(240)
    M=C1.get_point(300)

    hexa1=Polygon(K,C,A,G,O,Q)
    hexa2=Polygon(J,E,D,H,L,M)

    I.put_mark(0.2,90,"\( I\)",automatic_place=(pspict,"S"))

    K.put_mark(0.2,0,"\( K\)",automatic_place=(pspict,"W"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,135,"\( A\)",automatic_place=(pspict,"corner"))
    G.put_mark(0.2,180,"\( G\)",automatic_place=(pspict,"E"))
    O.put_mark(0.2,225,"\( N\)",automatic_place=(pspict,"corner"))
    Q.put_mark(0.2,-45,"\( P\)",automatic_place=(pspict,"N"))

    J.put_mark(0.2,0,"\( J\)",automatic_place=(pspict,"W"))
    E.put_mark(0.2,45,"\( E\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,135,"\( D\)",automatic_place=(pspict,"corner"))
    H.put_mark(0.2,180,"\( H\)",automatic_place=(pspict,"E"))
    L.put_mark(0.2,225,"\( L\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,-45,"\( M\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(K,C,A,G,O,Q,J,E,D,H,L,M,I,hexa1,hexa2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
