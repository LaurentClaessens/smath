# -*- coding: utf8 -*-

import string
from phystricks import *

def QTCQooFtDgwk():
    pspict,fig = SinglePicture("QTCQooFtDgwk")
    pspict.dilatation(1)

    O=Point(0,0)
    r=3

    O.put_mark(0.2,0,"\( O\)",pspict=pspict,position="W")

    cercle=Circle(O,r)
    A=cercle.get_point(45)
    B=cercle.get_point(90)
    C=cercle.get_point(180)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    mid=[  seg.midpoint() for seg in triangle.edges  ]

    an=[90+45,180-45,-45]
    for i,P in enumerate(mid):
        P.put_mark(0.2,P.advised_mark_angle(pspict)+an[i],"\( {}\)".format(string.ascii_uppercase[i+4]),pspict=pspict,position="corner")
        
    mediatrices=[  Segment(O,m).dilatation(1.5) for m in mid ]

    #for i,edge in enumerate(triangle.edges) :
    #    edge.divide_in_two(n=i+1,d=0.1,l=0.3,pspict=pspict)

    for i in [0,1,2]:
        cot=triangle.edges[i]
        med=mediatrices[i]
        med.parameters.style="dashed"
        #rh=RightAngle(med,cot,0,0)
        #pspict.DrawGraphs(rh)

    pspict.DrawGraphs(triangle,mediatrices,O,mid)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
