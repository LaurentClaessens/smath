# -*- coding: utf8 -*-
from phystricks import *
def KQGKooQyKvWm():
    pspict,fig = SinglePicture("KQGKooQyKvWm")
    pspict.dilatation(1)

    O=Point(0,0)

    names_list=["A","K","L","N","M"]
    names_list=["O","A","B","A'","B'"]

    O.put_mark(0.2,180,"\( "+names_list[0]+"\)",automatic_place=(pspict,""))

    P1=Point(5,1)
    P2=Point(5,3)
    s1=Segment(P1,O)
    s2=Segment(O,P2)
    
    p1=0.3
    p2=0.6
    A=s2.get_point_proportion(p1)
    B=s2.get_point_proportion(p2)
    Ap=s1.get_point_proportion(p2)

    parall=Segment(A,Ap).parallel_trough(B)
    Bp=Intersection(parall,s1)[0]

    A.put_mark(0.2,None,"\("+names_list[1]+" \)",automatic_place=(pspict,""))
    B.put_mark(0.2,None,"\("+names_list[2]+" \)",automatic_place=(pspict,""))
    Ap.put_mark(0.2,None,"\("+names_list[4]+" \)",automatic_place=(pspict,""))
    Bp.put_mark(0.2,None,"\("+names_list[3]+" \)",automatic_place=(pspict,""))

    #A.put_mark(0.2,None,"\("+"A"+" \)",automatic_place=(pspict,""))
    #B.put_mark(0.2,None,"\("+"B"+" \)",automatic_place=(pspict,""))
    #Ap.put_mark(0.2,None,"\("+"A'"+" \)",automatic_place=(pspict,""))
    #Bp.put_mark(0.2,Ap.advised_mark_angle,"\("+"B'"+" \)",automatic_place=(pspict,""))


    pspict.DrawGraphs(  Segment(A,Ap),Segment(B,Bp)  )

    for p in [A,B,Ap,Bp,O]:
        p.parameters.symbol=""
    pspict.DrawGraphs(s1,s2,A,B,Ap,Bp,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

