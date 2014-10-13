# -*- coding: utf8 -*-
from phystricks import *
def YDAooMNHhCN():
    pspicts,figs = IndependentPictures("YDAooMNHhCN",2)

    for psp in pspicts:
        psp.dilatation(1.5)

    a=2
    b=1
    l=a+b
    A=Point(0,0)
    B=A+(l,0)
    C=B-(0,l)
    D=C-(l,0)

    grand=Polygon(A,B,C,D)

    M=A+(b,0)
    N=B-(0,b)
    O=D+(a,0)
    P=D+(0,b)

    carre=Polygon(M,N,O,P)

    A.put_mark(0.2,90+45,"\( A\)",automatic_place=(pspicts,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspicts,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspicts,"corner"))
    D.put_mark(0.2,180+45,"\( D\)",automatic_place=(pspicts,"corner"))
    M.put_mark(0.2,90,"\( M\)",automatic_place=(pspicts,"S"))
    N.put_mark(0.2,0,"\( N\)",automatic_place=(pspicts,"W"))
    O.put_mark(0.2,-90,"\( O\)",automatic_place=(pspicts,"N"))
    P.put_mark(0.2,180,"\( P\)",automatic_place=(pspicts,"E"))

    a1=Angle(M,P,A)
    a2=Angle(N,M,B)
    b1=Angle(A,M,P)
    b2=Angle(B,N,M)

    a1.put_mark(0.2,a1.advised_mark_angle,"\( \\alpha\)",automatic_place=(pspicts,"corner"))
    a2.put_mark(0.2,a2.advised_mark_angle,"\( \\alpha\)",automatic_place=(pspicts,"corner"))
    b1.put_mark(0.2,b1.advised_mark_angle,"\( \\beta\)",automatic_place=(pspicts,"corner"))
    b2.put_mark(0.2,b2.advised_mark_angle,"\( \\beta\)",automatic_place=(pspicts,"corner"))

    cen=[]
    cen.append(Segment( A,M  ).center())
    cen[-1].put_mark(0.2,90,"\( a\)",automatic_place=(pspicts,"S"))
    cen.append(Segment( M,B  ).center())
    cen[-1].put_mark(0.2,90,"\( b\)",automatic_place=(pspicts,"S"))
    cen.append(Segment( B,N  ).center())
    cen[-1].put_mark(0.2,0,"\( a\)",automatic_place=(pspicts,"W"))
    cen.append(Segment( N,C  ).center())
    cen[-1].put_mark(0.2,0,"\( b\)",automatic_place=(pspicts,"W"))
    cen.append(Segment( C,O  ).center())
    cen[-1].put_mark(0.2,-90,"\( a\)",automatic_place=(pspicts,"N"))
    cen.append(Segment( D,O  ).center())
    cen[-1].put_mark(0.2,-90,"\( b\)",automatic_place=(pspicts,"N"))
    cen.append(Segment( D,P  ).center())
    cen[-1].put_mark(0.2,180,"\( a\)",automatic_place=(pspicts,"E"))
    cen.append(Segment( P,A  ).center())
    cen[-1].put_mark(0.2,180,"\( b\)",automatic_place=(pspicts,"E"))
    cen.append(Segment( M,P  ).center())
    cen[-1].put_mark(0.2,cen[-1].advised_mark_angle,"\( c\)",automatic_place=(pspicts,"corner"))
    for p in cen:
        p.parameters.symbol=""
    cen2=[ cen[2],cen[3],cen[4],cen[5],cen[6] ]

    K=Point( O.x,P.y )
    L=Point(O.x,N.y)
    R=Point(O.x,B.y)

    com1=Segment(R,O)
    com2=Segment(L,N)
    com3=Segment(P,K)
    com4=Segment(P,O)
    com5=Segment(O,N)

    R.put_mark(0.2,90,"\( R\)",automatic_place=(pspicts,"S"))
    L.put_mark(0.2,180,"\( L\)",automatic_place=(pspicts,"E"))
    K.put_mark(0.2,90+45,"\( K\)",automatic_place=(pspicts,"corner"))

    for pspict in pspicts :
        pspict.DrawGraphs(grand,A,B,C,D,O,P)
    pspicts[0].DrawGraphs(M,N)
    pspicts[0].DrawGraphs(carre,a1,a2,b1,b2,cen)

    pspicts[1].DrawGraphs(N,com1,com2,com3,com4,com5,R,K,L,cen2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
