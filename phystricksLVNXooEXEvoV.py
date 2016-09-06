# -*- coding: utf8 -*-
from phystricks import *
def LVNXooEXEvoV():
    pspicts,figs = IndependentPictures("LVNXooEXEvoV",5)

    for psp in pspicts:
        psp.dilatation(0.7)

    triangles=[]
    triangles.append(  Polygon(  Point(0,0),Point(2,0),Point(2.5,-2)  )  )
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
    med1=triangles[0].edges[0].bisector(code=(1,0.2,0.3,45,pspicts))
    pspicts[0].DrawGraphs(med1.added_objects[pspicts[0]])
    med1=med1+Vector(0,-0.5)
    rh=RightAngle(triangles[0].edges[0],med1,1,0)
    pspicts[0].DrawGraphs(med1,rh)

    # Deuxième figure
    line=triangles[1].edges[1].orthogonal_trough(triangles[1].vertices[0]).dilatation(1.3)
    rh=RightAngle( triangles[1].edges[1],line,1,0  )
    pspicts[1].DrawGraphs(line,rh)

    # Troisième figure
    cot=triangles[2].edges[0]
    P=triangles[2].vertices[2]
    line=cot.orthogonal_trough(P).dilatation(1.3)
    Q=Intersection(line,cot)[0]
    prol=cot.dilatation(3)
    prol.parameters.style="dashed"
    rh=RightAngle(  prol,line,0,0 )
    pspicts[2].DrawGraphs(prol,line,rh)

    # Quatrième figure
    cot=triangles[3].edges[1]
    P=triangles[3].vertices[0]
    M=cot.midpoint()
    line=Segment(M,P).dilatation(1.3)
    s1=Segment(triangles[3].vertices[2],M)
    s2=Segment(triangles[3].vertices[1],M)
    s1.put_code(n=1,d=0,l=0.2,pspict=pspicts[3])
    s2.put_code(n=1,d=0,l=0.2,pspict=pspicts[3])
    pspicts[3].DrawGraphs(line,s1,s2)

    # Cinquième figure
    cot=triangles[4].edges[2]
    P=triangles[4].vertices[1]
    bis=cot.bisector(code=(1,0.2,0.3,45,pspicts))
    line=cot.orthogonal_trough(P).dilatation(1.3)
    rh=RightAngle(line,cot,0,0)
    pspicts[4].DrawGraphs(bis.added_objects[pspicts[4]],line,rh)

    for i,pspict in enumerate(pspicts):
        pspict.DrawGraphs(triangles[i])
        pspict.comment="Il y a des codages de bissectrices ou un truc du genre à vérifier"
    
    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
