# -*- coding: utf8 -*-
# Ce fichier est seulement utilisé pour son image, et non pour sa figure.

from phystricks import *
def PythagoreeBqLDU():
    pspict,fig = SinglePicture("PythagoreeBqLDU")
    pspict.dilatation(1)

    lx=3
    ly=2
    A=Point(1,1)
    B=Point(A.x+lx,A.y+ly)
    C=Point(B.x,A.y)
    A.put_mark(0.2,135,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict)

    Ay=A.projection(pspict.axes.single_axeY)
    By=B.projection(pspict.axes.single_axeY)
    Ax=A.projection(pspict.axes.single_axeX)
    Bx=B.projection(pspict.axes.single_axeX)

    By.put_mark(0.2,180,"\( y_B\)",pspict=pspict)
    Ay.put_mark(0.2,180,"\( y_A\)",pspict=pspict)
    Ax.put_mark(0.2,-90,"\( x_A\)",pspict=pspict)
    Bx.put_mark(0.2,-90,"\( x_B\)",pspict=pspict)

    AB=Segment(A,B)
    AC=Segment(A,C)
    BC=Segment(B,C)
    AB.parameters.color="red"
    AC.parameters.style="dashed"
    BC.parameters.style="dashed"

    s=[]

    s.append(Segment(B,By))
    s.append(Segment(A,Ay))
    s.append(Segment(A,Ax))
    s.append(Segment(C,Bx))

    for seg in s:
        seg.parameters.color="blue"
        seg.parameters.style="dotted"


    measureBC=MeasureLength(BC,-0.2)
    measureBC.put_mark(0.2,measureBC.advised_mark_angle(pspict),"\( y_B-y_A\)",pspict=pspict)
    #measureBC.put_mark(0.7,0,"\( B_y-A_y\)")
    measureAC=MeasureLength(AC,0.2)
    measureAC.put_mark(0.3,measureAC.advised_mark_angle(pspict),"\( x_B-x_A\)",pspict=pspict)

    pspict.DrawGraphs(By,Ay,Ax,Bx,AB,AC,BC,s,measureBC,measureAC,A,B,C)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

# TODO : il me semble que les angles des marques des points ne fonctionnent pas bien.
