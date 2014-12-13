# -*- coding: utf8 -*-
from phystricks import *
def QFpJtQc():
    pspict,fig = SinglePicture("QFpJtQc")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(0.6)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(2,3)

    triangle=Polygon(A,B,C)

    M=Segment(A,C).get_point_proportion(0.3)

    s=Segment(C,B).fix_origin(M)
    N=Intersection(s,Segment(A,B))[0]
    t=Segment(A,C).fix_origin(N)
    G=Intersection(t,Segment(C,B))[0]

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspict,"S"))
    M.put_mark(0.2,M.advised_mark_angle,"\( M\)",automatic_place=(pspict,"corner"))
    N.put_mark(0.2,-90,"\( N\)",automatic_place=(pspict,"N"))
    G.put_mark(0.2,Segment(C,B).angle().degree+90,"\( G\)",automatic_place=(pspict,"corner"))

    parallelogram=Polygon(C,G,N,M)

    pspict.DrawGraphs(A,B,C,M,triangle,N,G,parallelogram)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
