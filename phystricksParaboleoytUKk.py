from phystricks import *
def ParaboleoytUKk():
    pspict,fig = SinglePicture("ParaboleoytUKk")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(2*x**2+4*x+2).graph(-2.5,0.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
