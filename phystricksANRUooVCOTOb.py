# -*- coding: utf8 -*-
from phystricks import *
def ANRUooVCOTOb():
    pspict,fig = SinglePicture("ANRUooVCOTOb")
    pspict.dilatation(1)

    O=Point(0,0)
    r=3
    angle=60*degree
    base=Segment( Point(-2*r,-r),Point(2*r,-r)  )

    tarte=Circle(  O,r  )

    vecteur=  cos(angle.radian),sin(angle.radian)   

    P=tarte.get_point(  90+angle.degree )
    P.put_mark(0.2,P.advised_mark_angle,"\( P\)",automatic_place=(pspict,"corner"))
    v=Segment(P,  P+vecteur   ).dilatation(3)
    Q=Intersection(v,base)[0]
    Q.put_mark(0.2,-90,"\( Q\)",automatic_place=(pspict,"N"))

    Pp=tarte.get_point(  -90+angle.degree )
    Pp.put_mark(0.2,P.advised_mark_angle,"\( P'\)",automatic_place=(pspict,"corner"))
    vp=Segment(Pp,  Pp+vecteur   ).dilatation(3)
    Qp=Intersection(vp,base)[0]
    Qp.put_mark(0.2,-90,"\( Q'\)",automatic_place=(pspict,"N"))
    wp=Segment(Pp,Qp)

    import numpy
    X=numpy.linspace(  Q.x,Qp.x,10,endpoint=True )
    for x in X:
        A=Point(x,-r)
        seg=Segment(A,A+vecteur).dilatation(1.5)
        seg.parameters.color="blue"
        pts=Intersection(seg,tarte)
        if len(pts)==2:
            I=pts[0]
            J=pts[1]
            print("I",I.x,I.y)
            print("J",J.x,J.y)
            klmklm
            S=Segment(I,J)
            S.parameters.color='green'
            seg.parameters.color="red"
            t=Segment(seg.F,I)
            t.parameters.color="purple"
            pspict.DrawGraphs(I,J,S,t)
        pspict.DrawGraphs(seg)

    pspict.DrawGraphs(tarte,base,Q,Qp)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
