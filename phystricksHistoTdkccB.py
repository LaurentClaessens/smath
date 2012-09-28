from phystricks import *
def HistoTdkccB():
    pspict,fig = SinglePicture("HistoTdkccB")
    pspict.dilatation(1)

    H=Histogram([(0,10,36),(10,35,24),(35,50,10),(35,50,10),(50,100,19),(100,200,11)])

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
