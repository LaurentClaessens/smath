from phystricks import *
def ParaboleUneSolPktmCR():
    pspict,fig = SinglePicture("ParaboleUneSolPktmCR")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction((x+1)**2).graph(-3,1)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
