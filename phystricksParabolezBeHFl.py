from phystricks import *
def ParabolezBeHFl():
    pspict,fig = SinglePicture("ParabolezBeHFl")
    pspict.dilatation(0.7)

    x=var('x')
    f=phyFunction(x**2+2*x-3).graph(-3.5,1.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
