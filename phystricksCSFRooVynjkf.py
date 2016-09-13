# -*- coding: utf8 -*-
from phystricks import *
def CSFRooVynjkf():
    pspicts,figs = IndependentPictures("CSFRooVynjkf",2)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    O=Point(0,0)
    B=O+(-2,-1)
    C=O+O-B
    cer=CircleOA(O,B)
    A=cer.get_point(90)
    cer.parameters.style="dashed"

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspicts=pspicts)
    O.put_mark(0.2,angle=-90,added_angle=0,text="\( O\)",pspicts=pspicts)

    rh=RightAngleAOB(B,A,C,r=0.3,n1=0,n2=1)
    trig.edges[1].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspicts=pspicts)

    AO=Segment(A,O)
    AO.put_code(n=2,d=0.1,l=0.2,pspicts=pspicts)


    no_symbol(trig.vertices)


    pspicts[0].DrawGraphs(O,A,B,C,trig.edges[1],AO)
    pspicts[1].DrawGraphs(O,trig,rh)
    
    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
