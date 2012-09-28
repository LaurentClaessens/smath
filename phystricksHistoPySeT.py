from phystricks import *
def HistoPySeT():
    pspict,fig = SinglePicture("HistoPySeT")
    pspict.dilatation(1)

    H=Histogram([(0,500,0.37),(500,1000,0.36),(1000,1500,0.18),(1500,3000,0.09)])

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
