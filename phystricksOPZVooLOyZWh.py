# -*- coding: utf8 -*-
from phystricks import *
def OPZVooLOyZWh():
    pspict,fig = SinglePicture("OPZVooLOyZWh")
    pspict.dilatation(0.7)

    c=3
    A=Point(0,0)
    L=A+(c,0)
    B=L+(c,0)
    D=A+(0,c)
    K=D+(c,0)
    C=K+(c,0)

    car1=Polygon(D,K,L,A)
    car2=Polygon(K,C,B,L)
    d1=Segment(D,L)
    d2=Segment(K,B)
    dig=Segment(A,C)

    I=Intersection(d1,dig)[0]
    J=Intersection(d2,dig)[0]

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    L.put_mark(0.2,-90,"\( L\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    K.put_mark(0.2,90,"\( K\)",automatic_place=(pspict,"S"))
    D.put_mark(0.2,90+45,"\( D\)",automatic_place=(pspict,"corner"))
    I.put_mark(0.2,90,"\( I\)",automatic_place=(pspict,"S"))
    J.put_mark(0.2,90,"\( J\)",automatic_place=(pspict,"S"))

    A.parameters.symbol=''
    B.parameters.symbol=''
    C.parameters.symbol=''
    D.parameters.symbol=''
    K.parameters.symbol=''
    L.parameters.symbol=''
    I.parameters.symbol=''
    J.parameters.symbol=''

    pspict.DrawGraphs(A,B,C,D,K,L,I,J,car1,car2,d1,d2,dig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
