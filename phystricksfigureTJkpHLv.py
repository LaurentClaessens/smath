# -*- coding: utf8 -*-
from phystricks import *
def figureTJkpHLv():
    pspict,fig = SinglePicture("figureTJkpHLv")
    pspict.dilatation(0.3)

    pspict.specific_needs="""\usepackage[cdot,thinqspace,amssymb]{SIunits}
                \\newcommand{\\vect}[1]{\overrightarrow{#1}}"""

    l=20
    O=Point(0,0)
    v1=AffineVector(O,O+(0,15))
    v2=AffineVector(v1.F,v1.F+(5,0))
    b1=Segment(O,O+(l,0))
    b2=Segment(b1.I+(0,20),b1.F+(0,20))

    v1.put_mark(0.2,v1.advised_mark_angle,"\unit{15}{\kilo\meter\per\hour}",automatic_place=pspict)
    v2.put_mark(0.2,v2.advised_mark_angle,"\unit{5}{\kilo\meter\per\hour}",automatic_place=pspict)

    v=v1+v2
    v.parameters.color="red"
    v.put_mark(0.2,-45,"\( \\vect{ v }\)",automatic_place=pspict)

    b1.parameters.color="blue"
    b2.parameters.color="blue"

    pspict.DrawGraphs(v1,v2,b1,b2,v)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
