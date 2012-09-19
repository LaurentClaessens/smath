from phystricks import *
def EvZZys():
    pspict,fig = SinglePicture("EvZZys")
    pspict.dilatation(1)

    x=var('x')
    A=Point(-1/2,1)
    B=Point(4,2)
    C=Point(-1,-2)
    D=Point(5,3)

    A.put_mark(0.1,A.angle(),"$A$",automatic_place=pspict)
    B.put_mark(0.1,B.angle(),"$B$",automatic_place=pspict)
    C.put_mark(0.1,C.angle(),"$C$",automatic_place=pspict)
    D.put_mark(0.1,D.angle(),"$D$",automatic_place=pspict)


    pspict.DrawGraphs(A,B,C,D)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
