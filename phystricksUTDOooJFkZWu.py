# -*- coding: utf8 -*-
from phystricks import *
def UTDOooJFkZWu():
    pspict,fig = SinglePicture("UTDOooJFkZWu")
    pspict.dilatation(0.5)

    O=Point(0,0)
    cer=Circle( O,4 )
    P=cer.get_point(30)
    ray=Segment(O,P)
    ray.parameters.style="dashed"
    ray.put_mark(0.2,angle=None,added_angle=0,text="\SI{4}{\centi\meter}",pspict=pspict)

    O.put_mark(0.2,angle=90+45,added_angle=0,text="\( O\)",pspict=pspict)

    pspict.DrawGraphs(cer,ray)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
