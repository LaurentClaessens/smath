# -*- coding: utf8 -*-
from phystricks import *
def LVNXooEXEvoV():
    pspicts,figs = IndependentPictures("LVNXooEXEvoV",5)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    triangles=[]
    triangles.append(  Polygon(  Point(0,0),Point(1,0),Point(2,-2)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(1,1),Point(2,-1)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(0.3,1),Point(1.5,-1)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(1,1),Point(1,-2)  )  )
    triangles.append(  Polygon(  Point(0,0),Point(1,2),Point(2,0)  )  )

    triangles[0].put_mark(0.2,["\( Q\)","\( C\)","\( M\)"],pspict=pspicts)
    triangles[1].put_mark(0.2,["\( T\)","\( A\)","\( K\)"],pspict=pspicts)
    triangles[2].put_mark(0.2,["\( R\)","\( N\)","\( T\)"],pspict=pspicts)
    triangles[3].put_mark(0.2,["\( B\)","\( D\)","\( O\)"],pspict=pspicts)
    triangles[4].put_mark(0.2,["\( F\)","\( E\)","\( H\)"],pspict=pspicts)

    
    # Première figure
    med1=triangles[0].edges[0].bisector(code=(1,0.1,0.1,45,pspicts))
    pspicts[0].DrawGraphs(med1.added_objects)
    med1=med1+Vector(0,-0.5)
    rh=RightAngle(triangles[0].edges[0],med1,0.2,0,1)
    pspicts[0].DrawGraphs(med1,rh)

    # Deuxième figure
    line=triangles[1].edges[1].orthogonal_trough(triangles[1].)<++>

    for i,pspict in enumerate(pspicts):
        pspict.DrawGraphs(triangles[i])
    
    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
