from phystricks import *
def ParabolesfTKFw():
    pspict,fig = SinglePicture("ParabolesfTKFw")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(4*x**2/5-24*x/5+5).graph(0.5,5.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
