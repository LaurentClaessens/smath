# -*- coding: utf8 -*-
from phystricks import *
def DIDMooOJHGra():
    pspict,fig = SinglePicture("DIDMooOJHGra")
    pspict.dilatation(0.7)

    lb=3
    alpha=30
    A=Point(0,0)
    cer=Circle(A,lb)
    D=cer.get_point(-90-alpha)
    E=cer.get_point(-90+alpha)
    B=(A+D)*0.5
    C=(A+E)*0.5
    lc=Segment(D,E).length()
    F=D+(0,-lc)
    G=E+(0,-lc)

    poly=Polygon(A,E,G,F,D)
    s1=Segment(B,C)
    s2=Segment(E,D)

    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,90+45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,180,"\( D\)",automatic_place=(pspict,"E"))
    E.put_mark(0.2,0,"\( E\)",automatic_place=(pspict,"W"))
    F.put_mark(0.2,180+45,"\( F\)",automatic_place=(pspict,"corner"))
    G.put_mark(0.2,-45,"\( G\)",automatic_place=(pspict,"corner"))

    for P in [A,B,C,D,E,F,G]:
        P.parameters.symbol=""

    m1=[  s.get_code(n=2,d=0.1,l=0.3,angle=45,pspict=pspict) for s in  [ Segment(A,B), Segment(B,D),Segment(A,C),Segment(C,E) ]  ]
    m2=[  s.get_code(n=1,d=0.1,l=0.3,angle=45,pspict=pspict) for s in  [ Segment(D,E), Segment(D,F),Segment(E,G) ]  ]

    rh1=RightAngle(  Segment(D,E),Segment(D,F),r=0.3, n1=1,n2=1 )
    rh2=RightAngle(  Segment(D,E),Segment(E,G),r=0.3, n1=0,n2=1 )

    pspict.DrawGraphs(poly,s1,s2,A,B,C,D,E,F,G,m1,m2,rh1,rh2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
