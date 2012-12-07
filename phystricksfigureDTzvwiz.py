# -*- coding: utf8 -*-
from phystricks import *
def figureDTzvwiz():
    pspict,fig = SinglePicture("figureDTzvwiz")
    pspict.dilatation(0.3)

    pspict.specific_needs="""\usepackage[cdot,thinqspace,amssymb]{SIunits}
                \\newcommand{\\vect}[1]{\overrightarrow{#1}}"""

    l=20
    O=Point(0,0)
    v1=AffineVector(O,O+(0,15))
    v2=AffineVector(v1.F,v1.F+(5,0))
    b1=Segment(O,O+(l,0))
    b2=Segment(b1.I+(0,20),b1.F+(0,20))


    v=v1+v2
    v.parameters.color="red"

    b1.parameters.color="blue"
    b2.parameters.color="blue"

    A=v1.F
    B=v.F
    Ap=Intersection(b2,v1)[0]
    Bp=Intersection(b2,v)[0]

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,0,"\( B\)",automatic_place=pspict)
    Ap.put_mark(0.2,90,"\( A'\)",automatic_place=pspict)
    Bp.put_mark(0.2,90,"\( B'\)",automatic_place=pspict)

    l1=Segment(A,Ap)
    l2=Segment(B,Bp)
    l1.parameters.style="dashed"
    l2.parameters.style="dashed"


    pspict.DrawGraphs(v1,v2,b1,b2,v,A,B,Ap,Bp,l1,l2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
