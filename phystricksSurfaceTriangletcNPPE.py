from phystricks import *
def SurfaceTriangletcNPPE():
    pspict,fig = SinglePicture("SurfaceTriangletcNPPE")
    pspict.dilatation(2)

    pspict.specific_needs="""\usepackage[cdot,thinqspace,amssymb]{SIunits}"""

    h=2
    d=3
    x=1.5
    A=Point(0,0)
    B=Point(d,0)
    C=Point(d,h)
    M=Point(x,0)
    Mp=Point(x,1)
    AB=Segment(A,B)
    BC=Segment(B,C)
    AC=Segment(A,C)
    Q=Intersection(AC,Segment(M,Mp))[0]
    MQ=Segment(M,Q)

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,45,"\( C\)",automatic_place=pspict)
    Q.put_mark(0.2,135,"\( Q\)",automatic_place=pspict)
    M.put_mark(0.2,-45,"\( M\)",automatic_place=pspict)
    triangle=Polygon(A,M,Q)
    triangle.parameters.filled()
    triangle.parameters.fill.color="green"

    measureMQ=MeasureLength(MQ,0.2)
    measureMQ.put_mark(0.3,measureMQ.advised_mark_angle,"$h$")

    measureBC=MeasureLength(BC,0.1)
    measureBC.put_mark(0.4,measureBC.advised_mark_angle,"$\unit{2}{\centi\meter}$")

    measureAM=MeasureLength(Segment(A,M),0.1)
    measureAM.put_mark(0.3,measureAM.advised_mark_angle,"$\unit{x}{\centi\meter}$")

    measureAB=MeasureLength(AB,0.5)
    measureAB.put_mark(0.3,measureAB.advised_mark_angle,"$\unit{3}{\centi\meter}$")

    pspict.DrawGraphs(triangle,A,B,C,AB,BC,AC,Q,M,MQ,measureMQ,measureBC,measureAM,measureAB)
    fig.conclude()
    fig.write_the_file()
