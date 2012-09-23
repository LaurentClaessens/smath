from phystricks import *
def ParabolezmMGdN():
    pspict,fig = SinglePicture("ParabolezmMGdN")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction( (x+1)**2+1 ).graph(-2,0.25)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
