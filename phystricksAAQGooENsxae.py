# -*- coding: utf8 -*-
from phystricks import *
def AAQGooENsxae():
    pspict,fig = SinglePicture("AAQGooENsxae")
    pspict.dilatation(0.6)

    O=Point(0,0)
    cer=Circle(O,2)
    P=cer.get_point(0)
    R=cer.get_point(120)

    r1=Segment(O,P)
    r2=Segment(R,O)
    lune=cer.graph(0,120)
    hach=CustomSurface(r1,lune,r2)
    hach.parameters.filled()
    hach.parameters.fill.color="lightgray"

    R.put_mark(0.2,angle=None,added_angle=0,text="\( R\)",pspict=pspict)
    P.put_mark(0.2,angle=None,added_angle=0,text="\( P\)",pspict=pspict)
    O.put_mark(0.2,angle=180+45,added_angle=0,text="\( O\)",pspict=pspict)

    no_symbol(R,O,P)
    pspict.DrawGraphs(hach,R,P,O,cer,r1,r2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
