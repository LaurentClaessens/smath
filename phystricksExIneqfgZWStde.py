from phystricks import *
def ExIneqfgZWStde():
    pspict,fig = SinglePicture("ExIneqfgZWStde")
    pspict.dilatation(1)

    x=var('x')
    mx=-6
    Mx=2.7
    intersections=[  Point(-5.5,1.5),Point(-3.5,1),Point(-1,1),Point(1.5,-1) ]
    pts1=intersections[:]
    pts1.extend([Point(-4.5,-1),Point(-2,3),Point(1,-1),Point(2.5,0)])
    lag1=LagrangePolynomial(pts1)
    f=lag1.graph(mx,Mx)
    f.put_mark(0.1,0,"\( f\)",pspict=pspict)

    pts2=intersections[:]
    pts2.extend([Point(-4.5,2.5),Point(-2,0),Point(0,1.5),Point(2,-2)])
    lag2=LagrangePolynomial(pts2)
    g=lag2.graph(mx,Mx)
    g.put_mark(0.1,0,"\( g\)",pspict=pspict)
    g.parameters.color="green"

    pspict.DrawGraphs(f,g)

    pts=Intersection(f,g,only_real=True)
    pts=[P for P in pts if P.x.is_real()]   # Because there are complex solutions.

    for P in [ Q for Q in pts if Q.x>mx and Q.x<Mx ]:
        R=Point(P.x,0)
        seg=Segment(P,R)
        seg.parameters.color="red"
        seg.parameters.style="dashed"
        seg.put_arrow()
        R.parameters.color="cyan"
        pspict.DrawGraphs(seg,P,R)

    X=[mx]
    X.extend([ Q.x for Q in pts if Q.x>mx and Q.x<Mx ])
    X.append(Mx)
    for i,x in enumerate(X[:-1]):
        m=(x+X[i+1])/2
        if f(m)<g(m):
            seg=Segment(Point(x,0),Point(X[i+1],0))
            seg.wave(0.1,0.1)
            seg.parameters.color="cyan"
            pspict.DrawGraphs(seg)


    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
