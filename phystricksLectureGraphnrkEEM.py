from phystricks import *
def LectureGraphnrkEEM():
    pspict,fig = SinglePicture("LectureGraphnrkEEM")
    pspict.dilatation_X(3)

    x=var('x')
    f=phyFunction(-3*x**3/2 + 6*x**2/2 + 3*x/2 - 3/2).graph(-1,2.5)

    pspict.axes.single_axeX.Dx=0.5
    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
