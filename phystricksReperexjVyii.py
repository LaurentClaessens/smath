from phystricks import *
def ReperexjVyii():
    pspict,fig = SinglePicture("ReperexjVyii")
    pspict.dilatation(1)

    O=Point(0,0)
    I=Point(1,0)
    J=Point(0,1)

    OX=Segment(O,I)
    OY=Segment(O,J)

    O.put_mark(0.2,225,"\( O\)",pspict=pspict)
    I.put_mark(0.2,-90,"\( I\)",pspict=pspict)
    J.put_mark(0.2,180,"\( J\)",pspict=pspict)

    M=Point(3,2)
    M.put_mark(0.2,45,"\( M\)",pspict=pspict)

    Mx=M.projection(OX)
    My=M.projection(OY)
    Mx.put_mark(0.2,-90,"\( x_M\)",pspict=pspict)
    My.put_mark(0.2,180,"\( y_M\)",pspict=pspict)

    l1=Segment(M,Mx)
    l2=Segment(M,My)
    l1.parameters.color="blue"
    l1.parameters.style="dashed"
    l2.parameters=l1.parameters

    pspict.DrawGraphs(O,I,J,M,Mx,My,l1,l2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
