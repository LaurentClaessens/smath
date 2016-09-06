# -*- coding: utf8 -*-

from __future__ import division
from __future__ import unicode_literals
from phystricks import *

def JYAKooXjBUpt():
    pspicts,figs = IndependentPictures("JYAKooXjBUpt",4)
    for psp in pspicts:
        psp.dilatation(0.6)

    l1=5
    l2=4
    l3=3
    h=2

    A=Point(0,0)
    B=A+(l1,0)
    c1=Circle(A,l3)
    c2=Circle(B,l2)
    C=Intersection(c1,c2)[1]

    base1=Polygon(A,B,C)
    base1.put_mark(0.2,pspict=pspicts)

    K1=base1.edges[2].rotation(-90).fix_size(h,only_F=True).F
    L1=A+K1-C
    face1=Polygon(L1,K1,C,A)

    M1=base1.edges[1].rotation(-90).fix_size(h,only_F=True).F
    K2=C+M1-B
    face2=Polygon(C,K2,M1,B)

    L2=base1.edges[0].rotation(-90).fix_size(h,only_F=True).F
    M2=B+L2-A
    face3=Polygon(A,B,M2,L2)

    print(u"Les trois nombres suivants doivent être ",h)
    print( numerical_approx( Segment(C,K1).length  ))
    print(  numerical_approx(Segment(C,K2).length  ))
    print(  numerical_approx(Segment(B,M2).length  ))

    face1.parameters.color='red'
    face2.parameters.color='blue'
    face3.parameters.color='green'

    arc1=Circle( K2,l3 )
    arc2=Circle( M1,l1 )
    arc1.parameters.style="dashed"
    arc2.parameters.style="dotted"

    sols=Intersection(arc1,arc2,numerical=True)
    S=sols[1]

    base2=Polygon(K2,S,M1)

    no_symbol(  [f.vertices for f in [base1,base2,face1,face2,face3]]  )
    pspicts[2].comment="The three lateral faces have the same heigh"
    pspicts[0].DrawGraphs(base1)
    pspicts[1].DrawGraphs(face1,face2,face3,base1)

    face1.put_mark(0.2,points_names="DE  ",pspict=pspicts)
    face2.put_mark(0.2,points_names=" FG ",pspict=pspicts)
    face3.put_mark(0.2,points_names="  HI",pspict=pspicts)

    pspicts[2].DrawGraphs(face1,face2,face3,base1,arc1,arc2)
    pspicts[3].DrawGraphs(face1,face2,face3,base1,arc1,arc2,base2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
