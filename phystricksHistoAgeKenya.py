from phystricks import *
def HistoAgeKenya():
    pspict,fig = SinglePicture("HistoAgeKenya")
    pspict.dilatation(1)

    H=Histogram([(0,15,52),(15,65,47),(65,110,2)])

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
