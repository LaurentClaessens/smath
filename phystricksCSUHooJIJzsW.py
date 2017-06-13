from phystricks import *
def CSUHooJIJzsW():
    from communPhys import thales
    pspict,fig = SinglePicture("CSUHooJIJzsW")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    N=Point(2,2)
    M=Point(1,3)
    B,C=thales(  A,N,M, 0.53,'A',"N","M","B","C",pspict )

    m1=Segment(C,A).get_mark(0.2,None,"\( 3\)",pspict=pspict,position="corner")
    m2=Segment(B,C).get_mark(0.2,None,"\( 2\)",pspict=pspict,position="corner")
    m3=Segment(A,M).get_measure(-0.6,0.1,None,"\( 4.5\)",pspict=pspict,position="E")
    m4=Segment(M,N).get_mark(0.2,None,"\( 6\)",pspict=pspict,position="E")

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

