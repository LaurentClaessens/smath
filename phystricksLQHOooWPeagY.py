# -*- coding: utf8 -*-
from phystricks import *
def LQHOooWPeagY():
    pspict,fig = SinglePicture("LQHOooWPeagY")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.7)
    pspict.rotation(15)

    S=Point(0,0)
    T=Point(4,0)
    U=Point(3,4)

    trig=Polygon(S,T,U)
    trig.put_mark(0.2,points_names="STU",pspict=pspict)

    I=trig.edges[0].midpoint()
    I.put_mark(0.2,angle=None,added_angle=180,text="\( I\)",pspict=pspict)
    mediane=Segment(  trig.vertices[    2],I  )
    trig.edges[0].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)
    mediane.divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)
    K=mediane.midpoint()
    K.put_mark(0.2,angle=90+45,added_angle=0,text="\( K\)",pspict=pspict)

    H=Point(S.x,U.y)
    H.put_mark(0.2,angle=90+45,added_angle=0,text="\( H\)",pspict=pspict)
    h1=Segment(S,H)
    h2=Segment(H,U)
    for seg in [h1,h2]:
        seg.parameters.style="dashed"

    h1.put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,name="\SI{4}{\centi\meter}",pspict=pspict)

    s1=Segment(S,K)
    s2=Segment(K,T)

    rh=RightAngleAOB(U,H,S)

    gris=Polygon(S,K,T,U)
    gris.parameters.filled()
    gris.parameters.fill.color="lightgray"

    pspict.comment="le 4cm est bien placé à côté de HS et le triangle est penché de 15 degrés."
    no_symbol(trig.vertices,H)
    pspict.DrawGraphs(gris,trig,I,mediane,K,s1,s2,h1,h2,H,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
