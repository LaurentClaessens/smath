# -*- coding: utf8 -*-
from phystricks import *
def SHSRooHgvofo():
    pspicts,figs = IndependentPictures("SHSRooHgvofo",6)
    for psp in pspicts:
        psp.dilatation(0.7)

    triangles=[]
    triangles.append(  Polygon(  Point(0,0),Point(2,0),Point(2.5,-2)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(2,0),Point(0,1)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(0.3,1),Point(1.5,-1)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(1,1),Point(1,-2)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(1,2),Point(2,0)  )  )

    A=Point(0,0)
    B=Point(2,1)
    s=Segment(A,B).rotation(60)
    C=s.F
    triangles.append(  Polygon( A,B,C  )  )


    triangles[0].put_mark(0.2,["\( Q\)","\( C\)","\( M\)"],pspict=pspicts)
    triangles[1].put_mark(0.2,["\( T\)","\( A\)","\( K\)"],pspict=pspicts)
    triangles[2].put_mark(0.2,["\( R\)","\( N\)","\( T\)"],pspict=pspicts)
    triangles[3].put_mark(0.2,["\( B\)","\( D\)","\( O\)"],pspict=pspicts)
    triangles[4].put_mark(0.2,["\( F\)","\( E\)","\( H\)"],pspict=pspicts)
    triangles[5].put_mark(0.2,["\( A\)","\( B\)","\( C\)"],pspict=pspicts)

    
    # Première figure

    # Deuxième figure
    # Celui-ci est rectangle
    trig=triangles[1]
    rh=RightAnlge( trig.edges[0],trig.edges[2],0.3,0,0  )
    pspicts[1].DrawGraphs(rh)

    # Troisième figure

    # Quatrième figure

    # Cinquième figure
    # Isocèle

    # Cinquième figure
    # équilatéral



    for i,pspict in enumerate(pspicts):
        pspict.DrawGraphs(triangles[i])
    
    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
