from phystricks import *
def BpCNVm():
    pspict,fig = SinglePicture("BpCNVm")
    pspict.dilatation(1)

    x=var('x')
    A=Point(5,2)
    poly=Polygon( Point(0,0),Point(A.x,0),A,Point(0,A.y) )
    poly.parameters.hatched()
    poly.parameters.hatch.color="green"
    poly.edge.parameters.color="blue"
    X=Point(3,0)
    X.put_mark(0.2,-90,"$x$",automatic_place=(pspict,"N"))
    X.symbol="none"

    pspict.DrawGraphs(poly,X)
    pspict.axes.no_numbering()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
