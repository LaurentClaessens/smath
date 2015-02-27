# -*- coding: utf8 -*-
from phystricks import *
def KPWWooFyZHHV():
    pspicts,figs = IndependentPictures("KPWWooFyZHHV",4)

    for psp in pspicts:
        psp.dilatation(0.7)

    T=[Point(0,0)    , Point(1.5,-1.5) ,  Point(1.5,-1.5) ,  Point(0,0)]
    M=[Point(2,1)    , Point(0,0)  ,      Point(0,0)  ,      Point(3,3)]
    O=[Point(1.5,-2) , Point(1.7,0.5)  ,    Point(1.7,0.5)  , Point(3,-0.5)]
    S=Point(1,2)
    triangles=[  Polygon(T[i],M[i],O[i]) for i in range(0,3)  ]
    triangles.append( Polygon(O[-1],T[-1],S,M[-1]) )

    for i in range(0,3):
        triangles[i].put_mark(0.2,text_list=["\( T\)","\( M\)","\( O\)"],pspict=pspicts)
    triangles[-1].put_mark(0.2,text_list=["\( T\)","\( O\)","\( M\)","\( S\)"],pspict=pspicts)

    A=[  triangles[0].edges[1].midpoint(),triangles[1].edges[1].midpoint(),triangles[2].edges[2].midpoint(),triangles[3].edges[1].midpoint()  ]
    B=[  triangles[0].edges[2].midpoint(),triangles[1].edges[2].midpoint(),triangles[2].edges[1].midpoint(),triangles[3].edges[0].midpoint()  ]

    triangles[0].edges[1].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspicts)
    triangles[0].edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)
    triangles[1].edges[2].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspicts)

    triangles[3].edges[0].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)
    triangles[3].edges[1].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspicts)

    code1=Segment(  O[2],B[2]  ).get_code(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)
    code2=Segment(  O[2],A[2]  ).get_code(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)

    AB=[  Segment(A[i],B[i]).dilatation(1.5) for i in range(0,4)  ]

    no_symbol([trig.vertices for trig in triangles])

    for p in T:
        p.parameters.symbol=""
    for p in M:
        p.parameters.symbol=""
    for p in O:
        p.parameters.symbol=""
    for p in A:
        p.parameters.symbol=""
    for p in B:
        p.parameters.symbol=""
    S.parameters.symbol=""
    for i in range(0,4):
        A[i].put_mark(0.2,None,"\( A\)",automatic_place=(pspicts,"corner"))
        B[i].put_mark(0.2,None,"\( B\)",automatic_place=(pspicts,"corner"))
        pspicts[i].DrawGraphs(triangles[i],A[i],B[i],AB[i])

    pspicts[2].DrawGraphs(code1,code2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
