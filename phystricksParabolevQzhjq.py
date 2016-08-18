from phystricks import *
def ParabolevQzhjq():
    pspict,fig = SinglePicture("ParabolevQzhjq")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(x**2-4*x+3).graph(-0.3,4.3)
    P=[]
    P.append(Point(3,0))
    P.append(Point(0,3))
    P.append(Point(4,3))
    P.append(Point(1,0))
    S=Point(2,-1)
    S.put_mark(0.2,-45,"$S$",pspict=pspict)

    sym=Segment(Point(2,-2),Point(2,4))
    sym.parameters.color="red"
    sym.parameters.style="dashed"

    pspict.DrawGraphs(f,sym,P,S)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
