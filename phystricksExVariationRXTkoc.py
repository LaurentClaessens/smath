from phystricks import *
def ExVariationRXTkoc():
    pspict,fig = SinglePicture("ExVariationRXTkoc")
    pspict.dilatation(0.7)

    x=var('x')
    mx=-4.5
    Mx=4
    pts=[Point(-2.5,0),Point(-1,1),Point(2,0)]
    df=LagrangePolynomial(pts)
    f=phyFunction(df.sage.integrate(x)).graph(mx,Mx)
    f.put_mark(0.2,0,"\( f\)",pspict=pspict)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
