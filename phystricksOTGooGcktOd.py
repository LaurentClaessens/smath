# -*- coding: utf8 -*-
from phystricks import *
def OTGooGcktOd():
    pspict,fig = SinglePicture("OTGooGcktOd")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    A=Point(0,1)
    E=Circle(A,4).get_point(30)
    U=Circle(A,6).get_point(-20)
    trig1=Polygon(A,E,U)
    
    AE=Segment(A,E)
    AE.put_mark(0.2,AE.advised_mark_angle,"\unit{4.5}{\centi\meter}",automatic_place=(pspict,"corner"))
    EU=Segment(E,U)
    EU.put_mark(0.2,EU.advised_mark_angle,"\unit{5}{\centi\meter}",automatic_place=(pspict,"corner"))
    AU=Segment(A,U)
    AU.put_mark(0.2,AU.advised_mark_angle+180,"\unit{5.5}{\centi\meter}",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,180,"\( A\)",automatic_place=(pspict,"corner"))
    E.put_mark(0.2,90,"\( E\)",automatic_place=(pspict,"corner"))
    U.put_mark(0.2,-45,"\( U\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(trig1,AE.mark,EU.mark,AU.mark,A,E,U)

    Q=Point(U.x+1,U.y-2)
    O=Circle(Q,5.8).get_point(60)
    segII=Segment(Q,Point(Q.x,Q.y-2))
    PI=Circle(O,1).get_point(150)
    C=Intersection(  segII,Segment(O,PI) )[0]

    trig2=Polygon(Q,O,C)

    QO=Segment(Q,O)
    QO.put_mark(0.2,QO.advised_mark_angle+180,"\unit{4.5}{\centi\meter}",automatic_place=(pspict,"corner"))
    Q.put_mark(0.2,-45,"\( Q\)",automatic_place=(pspict,"corner"))
    O.put_mark(0.2,0,"\( O\)",automatic_place=(pspict,"W"))
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspict,"S"))

    angle1=Angle(O,Q,C)
    angle1.put_mark(0.5,angle1.advised_mark_angle,"\unit{20}{\degree}",automatic_place=(pspict,"center"))
    angle2=Angle(C,O,Q)
    angle2.put_mark(0.6,angle2.advised_mark_angle,"\unit{105}{\degree}",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(trig2,QO.mark,Q,O,C,angle1,angle2)

    I=Point(U.x-1,U.y-1)
    cercle=Circle(I,6.5)
    N=cercle.get_point(-80)
    V=cercle.get_point(-80-75)

    trig3=Polygon(I,N,V)
    angle3=Angle(V,I,N)
    angle3.put_mark(0.7,angle3.advised_mark_angle,"\unit{75}{\degree}",automatic_place=(pspict,"center"))

    I.put_mark(0.2,90,"\( I\)",automatic_place=(pspict,"S"))
    N.put_mark(0.2,-45,"\( N\)",automatic_place=(pspict,"corner"))
    V.put_mark(0.2,180,"\( V\)",automatic_place=(pspict,"E"))

    IV=Segment(I,V)
    IV.put_mark(0.2,IV.advised_mark_angle+180,"\unit{7}{\centi\meter}",automatic_place=(pspict,"corner"))
    IN=Segment(I,N)
    IN.put_mark(0.2,IN.advised_mark_angle,"\unit{6}{\centi\meter}",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(trig3,angle3,I,N,V,IV.mark,IN.mark)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
