from phystricks import *
def bDdpfh():
    pspict,fig = SinglePicture("bDdpfh")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(x**2).graph(-2,2)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
