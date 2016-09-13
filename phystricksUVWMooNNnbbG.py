# -*- coding: utf8 -*-
from phystricks import *
def UVWMooNNnbbG():
    pspict,fig = SinglePicture("UVWMooNNnbbG")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=A+(1,0)
    C=B+(0,-1)
    Cp=B+(0,1)
    D=C+(2,0)
    Dp=Cp+(2,0)
    E=B+(2,0)
    F=E+(2,0)
    G=F+(0,-3)
    H=A+G-F

    pol1=Polygon(A,B,C,D,E,F,G,H)
    pol2=Polygon(  [x+(F-A)+(2,0) for x in    [A,B,Cp,Dp,E,F,G,H]    ] )

    pol1.parameters.color='blue'
    pol1.edge_model.parameters.linewidth=2
    pol2.parameters.color='red'
    pol2.edge_model.parameters.linewidth=1.5

    #k1=Segment(A,G)
    #k1.parameters.linewidth=0.5
    #k2=Segment(G,H)
    #k2.parameters.linewidth=1

    pspict.DrawGraphs(pol1,pol2)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

