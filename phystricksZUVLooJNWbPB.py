# -*- coding: utf8 -*-
from phystricks import *
def ZUVLooJNWbPB():
    pspicts,figs = IndependentPictures("ZUVLooJNWbPB",2)
    for psp in pspicts :
        psp.dilatation(1)

    A=Point(0,0)
    B=A+(4,0)
    C=A+(1,2)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,pspict=pspicts)
    diag1=Segment(A,C)

    no_symbol(parall.vertices)

    a1=Angle(C,A,D,r=0.3)
    a2=Angle(B,A,C)
    c1=Angle(D,C,A,)
    c2=Angle(A,C,B,r=0.3)

    ma1=a1.get_mark(0.2,angle=None,text="\( a_1\)",automatic_place=(pspicts,""))
    ma2=a2.get_mark(0.2,angle=None,text="\( a_2\)",automatic_place=(pspicts,""))
    mc1=c1.get_mark(0.2,angle=None,text="\( c_1\)",automatic_place=(pspicts,""))
    mc2=c2.get_mark(0.2,angle=None,text="\( c_2\)",automatic_place=(pspicts,""))

    mma1=a1.get_mark(0.2,angle=None,text="\( b\)",automatic_place=(pspicts,""))
    mma2=a2.get_mark(0.2,angle=None,text="\( a\)",automatic_place=(pspicts,""))
    mmc1=c1.get_mark(0.2,angle=None,text="\( a\)",automatic_place=(pspicts,""))
    mmc2=c2.get_mark(0.2,angle=None,text="\( b\)",automatic_place=(pspicts,""))

    pspicts[0].DrawGraphs(parall,diag1,a1,a2,c1,c2,ma1,ma2,mc1,mc2)
    pspicts[1].DrawGraphs(parall,diag1,a1,a2,c1,c2,mma1,mma2,mmc1,mmc2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

