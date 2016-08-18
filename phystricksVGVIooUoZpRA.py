# -*- coding: utf8 -*-
from phystricks import *
def VGVIooUoZpRA():
    pspict,fig = SinglePicture("VGVIooUoZpRA")
    pspict.dilatation(1)

    O=Point(0,0)

    names_list=["O","R","S","U","T"]
    #names_list=["O","A","B","A'","B'"]

    O.put_mark(0.2,180,"\( "+names_list[0]+"\)",pspict=pspict)

    P1=Point(5,2)
    P2=Point(5,-1)
    s1=Segment(P1,O)
    s2=Segment(O,P2)

    p1=0.7
    p2=0.3
    p3=0.9
    A=s2.get_point_proportion(p1)
    B=s2.get_point_proportion(p3)
    Ap=s1.get_point_proportion(p2)

    parall=Segment(A,Ap).parallel_trough(B)
    Bp=Intersection(parall,s1)[0]

    A.put_mark(0.2,A.advised_mark_angle(pspict)+180,"\("+names_list[1]+" \)",pspict=pspict)
    B.put_mark(0.2,B.advised_mark_angle(pspict)+180,"\("+names_list[2]+" \)",pspict=pspict)
    Ap.put_mark(0.2,Ap.advised_mark_angle(pspict)+180,"\("+names_list[3]+" \)",pspict=pspict)
    Bp.put_mark(0.2,Ap.advised_mark_angle(pspict)+180,"\("+names_list[4]+" \)",pspict=pspict)

    pspict.DrawGraphs(  Segment(A,Ap),Segment(B,Bp)  )

    for p in [A,B,Ap,Bp,O]:
        p.parameters.symbol=""
    pspict.DrawGraphs(s1,s2,A,B,Ap,Bp,O)

    m1=Segment(Ap,A).get_mark(0.1,None,"\( 5\)",pspict=pspict)
    m2=Segment(A,O).get_mark(0.2,None,"\( 2\)",pspict=pspict)

    pspict.DrawGraphs(m1,m2)


    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

