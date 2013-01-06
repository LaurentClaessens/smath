# -*- coding: utf8 -*-
from phystricks import *
def figureKAzSlQr():
    pspict,fig = SinglePicture("figureKAzSlQr")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.3)

    A={3:2,4:4,7:1,8:1,16:2,17:1}
    B={1:3,2:1,11:2,12:3,10:1}

    segments=[]
    for x in range(0,20):
        if x in A.keys():
            s=Segment(Point(x,0),Point(x,A[x]))
            s.parameters.color="blue"
            s.parameters.add_option("linewidth","1.5mm")
            segments.append(s)
        if x in B.keys():
            s=Segment(Point(x,0),Point(x,B[x]))
            s.parameters.color="red"
            s.parameters.add_option("linewidth","1.5mm")
            segments.append(s)

    pspict.DrawGraphs(segments)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
