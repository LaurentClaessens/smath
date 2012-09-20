from phystricks import *
def ParaboleiLbviP():
    pspict,fig = SinglePicture("ParaboleiLbviP")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(-x**2+4).graph(-3,3)

    P=[]
    P.append(Point(2,0))
    P.append(Point(-2,0))
    P.append(Point(1,3))
    P.append(Point(3,-5))
    S=Point(0,4)
    S.put_mark(0.2,45,"$S$",automatic_place=pspict)

    sym=Segment(Point(0,-2),Point(0,1.5))
    sym.parameters.color="red"
    sym.parameters.style="dashed"


    pspict.DrawGraphs(f,sym,P,S)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
