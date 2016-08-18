# -*- coding: utf8 -*-
from phystricks import *
def IJFGooPLxXAV():
    pspict,fig = SinglePicture("IJFGooPLxXAV")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(0,3)
    C=Point(-4,0)
    S1=A+(7,0)
    S2=A+(0,-7)

    r1=sqrt(7**2+3**2)
    r2=sqrt(7**2+4**2)

    S3=Intersection(   Circle(B,r1),Circle(C,r2)  )[0]
    trig=Polygon(A,B,C)
    trig.put_mark(0.4,pspict=pspict)

    seg=[]
    seg.append(Segment(S3,B))
    seg.append(Segment(S3,C))
    seg.append(Segment(S2,A))
    seg.append(Segment(S2,C))
    seg.append(Segment(S1,B))
    seg.append(Segment(S1,A))

    S1.put_mark(0.2,angle=0,text="\( S_1\)",pspict=pspict)
    S2.put_mark(0.2,angle=-45,text="\( S_2\)",pspict=pspict)
    S3.put_mark(0.2,angle=180,text="\( S_3\)",pspict=pspict)

    trig.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\( 3\)",pspict=pspict)
    trig.edges[1].put_mark(0.2,angle=None,added_angle=180,text="\( 5\)",pspict=pspict)
    trig.edges[2].put_mark(0.2,angle=None,added_angle=180,text="\( 4\)",pspict=pspict)

    m7=Segment(S1,A).get_mark(0.2,angle=None,text="\( 7\)",pspict=pspict)


    no_symbol(A,B,C,S1,S2,S3)

    pspict.DrawGraphs(trig,seg,S1,S2,S3,m7)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
