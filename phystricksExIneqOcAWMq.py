from phystricks import *

def ExIneqOcAWMq():
    pspict,fig = SinglePicture("ExIneqOcAWMq")
    pspict.dilatation_X(1.5)
    pspict.dilatation_Y(0.7)

    x=var('x')
    k=2
    mx=-5
    Mx=2
    f=LagrangePolynomial([Point(-4,1), Point(-1.5,-2),Point(1,1)]).graph(mx,Mx)
    f.put_mark(0.2,0,"\( f\)",automatic_place=pspict)
    segk=Segment(Point(mx,k),Point(Mx,k))
    segk.parameters.color="brown"

    pspict.DrawGraphs(f,segk)
    pts=Intersection(segk,f)
    for P in [ Q for Q in pts if Q.x>mx and Q.x<Mx ]:
        R=Point(P.x,0)
        seg=Segment(P,R)
        seg.parameters.color="red"
        seg.parameters.style="dashed"
        seg.put_arrow()
        R.parameters.color="cyan"
        pspict.DrawGraphs(seg,P,R)

    P1=Point(pts[0].x,0)
    P2=Point(pts[1].x,0)
    segh=Segment(P1,P2)
    segh.wave(0.1,0.1)
    segh.parameters.color="cyan"
    pspict.DrawGraphs(segh)


    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
