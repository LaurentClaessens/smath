from phystricks import *
def ExEquationIntersectioniSHPTw():
    pspict,fig = SinglePicture("ExEquationIntersectioniSHPTw")
    pspict.dilatation(0.7)

    x=var('x')
    mx=-5.2
    Mx=2.5
    lag1=LagrangePolynomial( [Point(-5,-2),Point(-3.5,0),Point(-2.5,1),Point(-1.5,0),Point(2.5,0),Point(3.8,5)]   )+1.5
    f=lag1.graph(mx,Mx)
    f.put_mark(0.1,0,"\( f\)",automatic_place=pspict)

    lag2=LagrangePolynomial( [Point(-5,2),Point(-3.5,1),Point(-2.5,0),Point(0,1.5),Point(1,0),Point(3,-1)]   )
    g=lag2.graph(mx,Mx)
    g.put_mark(0.1,0,"\( g\)",automatic_place=pspict)
    g.parameters.color="green"

    pspict.DrawGraphs(f,g)

    pts=Intersection(f,g)
    for P in [ Q for Q in pts if Q.x>mx and Q.x<Mx ]:
        R=Point(P.x,0)
        seg=Segment(P,R)
        seg.parameters.color="red"
        seg.parameters.style="dashed"
        seg.put_arrow()
        R.parameters.color="cyan"
        pspict.DrawGraphs(seg,P,R)

    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
