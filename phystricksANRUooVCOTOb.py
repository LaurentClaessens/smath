# -*- coding: utf8 -*-
from phystricks import *

def ANRUooVCOTOb():
    pspict,fig = SinglePicture("ANRUooVCOTOb")
    pspict.dilatation(0.7)

    O=Point(0,0)
    r=3
    angle=60*degree
    base=Segment( Point(-2*r,-r),Point(2*r,-r)  )

    tarte=Circle(  O,r  )
    vecteur=  cos(angle.radian),sin(angle.radian)   

    
    P=tarte.get_point(  90+angle.degree )
    P.put_mark(0.2,None,"\( P\)",automatic_place=(pspict,"corner"))
    v=Segment(P,  P+vecteur   ).dilatation(3)
    Q=Intersection(v,base)[0]
    Q.put_mark(0.2,-90,"\( Q\)",automatic_place=(pspict,"N"))

    Pp=tarte.get_point(  -90+angle.degree )
    Pp.put_mark(0.2,P.advised_mark_angle(pspict),"\( P'\)",automatic_place=(pspict,"corner"))
    vp=Segment(Pp,  Pp+vecteur   ).dilatation(3)
    Qp=Intersection(vp,base)[0]
    Qp.put_mark(0.2,-90,"\( Q'\)",automatic_place=(pspict,"N"))
    wp=Segment(Pp,Qp)

    import numpy
    X=numpy.linspace(  Q.x,Qp.x,10,endpoint=True )
    for xx in X:
        A=Point(xx,-r)
        seg=Segment(A,A+vecteur).dilatation(1.5)
        seg.parameters.color="blue"
        pts=Intersection(seg,tarte)
        if len(pts)==2:
            I=pts[0]
            J=pts[1]
            S=Segment(I,J)
            pspict.DrawGraphs(S)

    Y=numpy.linspace(  -r,r,10,endpoint=True )
    for yy in Y:
        seg=Segment(  Point(0,yy),Point(5,yy)  )
        pts=Intersection(seg,tarte)
        if len(pts)==2:
            I=pts[0]
            J=pts[1]
            S=Segment(I,J)
            pspict.DrawGraphs(S)

    pspict.DrawGraphs(tarte)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

# Cette version est une version simplifiée qui m'a permis de remarquer une erreur lorsque Sage résout des systèmes d'équations.
# Par exemple ce système donne une solution qui n'est pas sur le cercle demandé :
#solve(    [   -1/3*sqrt(3)*y + 1/3*sqrt(3)*(-0.19245008972987399*sqrt(3) - 3) + x == 0,x^2 + y^2 - 9 == 0    ],[x,y]   )
def FUANooEQMEdF():
    pspict,fig = SinglePicture("FUANooEQMEdF")
    pspict.dilatation(1)

    O=Point(0,0)
    r=3
    angle=60*degree
    base=Segment( Point(-2*r,-r),Point(2*r,-r)  )

    tarte=Circle(  O,r  )
    vecteur=  cos(angle.radian),sin(angle.radian)   

    xx=0.192450089729874
    A=Point(xx,-r)
    seg=Segment(A,A+vecteur).dilatation(1.5)
    seg.parameters.color="blue"
    pts=Intersection(seg,tarte)
    for P in pts:
        pspict.DrawGraphs(P)

    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    pspict.DrawGraphs(tarte,base,seg,A)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

