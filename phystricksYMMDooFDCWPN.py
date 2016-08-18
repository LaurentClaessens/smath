# -*- coding: utf8 -*-
from phystricks import *
def YMMDooFDCWPN():
    pspict,fig = SinglePicture("YMMDooFDCWPN")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    L=5
    A=Point(0,0)
    B=Point(L,0)
    P=Segment(A,B).get_point_proportion(0.3)

    A.put_mark(0.2,angle=90+45,text="\( 0\)",pspict=pspict)
    B.put_mark(0.2,angle=45,text="\( 10\)",pspict=pspict)
    P.put_mark(0.2,angle=45,text="\( x\)",pspict=pspict)

    #C1=CircleAB(A,P).graph(0,180)       # le x
    #C2=CircleAB(P,B).graph(0,180)       # le 10-x
    #C3=CircleAB(A,B).graph(0,180)       # Le grand
    C1=CircleAB(A,P) # le x
    C2=CircleAB(P,B) # le 10-x
    C3=CircleAB(A,B) # Le grand

    pc1=C1.get_point(80)
    pc1.put_mark(0.03,angle=None,text="\( \mathcal{C}_1\)",pspict=pspict)
    pc2=C2.get_point(90+20)
    pc2.put_mark(0.03,angle=None,text="\( \mathcal{C}_2\)",pspict=pspict)
    pc3=C3.get_point(180-45)
    pc3.put_mark(0.03,angle=None,text="\( \mathcal{C}_3\)",pspict=pspict)

    seg=Segment(A,B)
    seg.parameters.style='dashed'

    no_symbol(pc1,pc2,pc3)

    pspict.comment="The marks on the circles are correctly placed (in the normal direction) and in mathcal font. They have no symbol"
    pspict.DrawGraphs(C1,C2,C3,seg,A,B,P,pc1,pc2,pc3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
