# -*- coding: utf8 -*-
from phystricks import *
def XDdastq():
    pspict,fig = SinglePicture("XDdastq")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    I=Point(0,0)
    r2=3
    r1=1.5

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

    B=Segment(A,C).center()
    P=Segment(O,Q).center()
    N=Segment(Q,K).center()
    F=Segment(C,K).center()


    hexa1=Polygon(K,C,A,G,O,Q)
    hexa2=Polygon(J,E,D,H,L,M)

    pointi=[]
    pointi.append(Segment(K,G))
    pointi.append(Segment(F,P))
    pointi.append(Segment(C,O))
    pointi.append(Segment(B,N))
    pointi.append(Segment(B,H))
    pointi.append(Segment(A,Q))
    pointi.append(Segment(P,H))

    for s in pointi:
        s.parameters.style="dashed"
    pspict.DrawGraphs(pointi)

    rempli=[]
    rempli.append(Segment(J,H))
    rempli.append(Segment(E,L))
    rempli.append(Segment(D,M))
    pspict.DrawGraphs(rempli)


    A.put_mark(0.2,135,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,90,"\( B\)",automatic_place=(pspict,"S"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,180,"\( D\)",automatic_place=(pspict,"E"))
    E.put_mark(0.2,0,"\( E\)",automatic_place=(pspict,"W"))
    F.put_mark(0.2,0,"\( F\)",automatic_place=(pspict,"corner"))
    G.put_mark(0.2,180,"\( G\)",automatic_place=(pspict,"E"))
    H.put_mark(0.2,125,"\( H\)",automatic_place=(pspict,"corner"))
    I.put_mark(0.2,90,"\( I\)",automatic_place=(pspict,"S"))
    K.put_mark(0.2,0,"\( K\)",automatic_place=(pspict,"W"))
    L.put_mark(0.2,180,"\( L\)",automatic_place=(pspict,"E"))
    M.put_mark(0.2,0,"\( M\)",automatic_place=(pspict,"W"))
    O.put_mark(0.2,225,"\( N\)",automatic_place=(pspict,"corner"))
    P.put_mark(0.2,-90,"\( P\)",automatic_place=(pspict,"N"))
    Q.put_mark(0.2,-45,"\( Q\)",automatic_place=(pspict,"N"))
    J.put_mark(0.2,45,"\( J\)",automatic_place=(pspict,"corner"))
    N.put_mark(0.2,-45,"\( N\)",automatic_place=(pspict,"corner"))
    pspict.DrawGraphs(F,B,P,N)

    pspict.DrawGraphs(K,C,A,G,O,Q,J,E,D,H,L,M,I,hexa1,hexa2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
