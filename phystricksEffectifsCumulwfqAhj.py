from phystricks import *
def EffectifsCumulwfqAhj():
    pspict,fig = SinglePicture("EffectifsCumulwfqAhj")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.5)

    l=[10,13,0,2,18,10,16,9,0,9,9,5,5,6,5,8,12,12,8,11,11,2,8,17,10,10,14]
    l.sort()
    points=[]
    for x in range(0,max(l)):
        points.append(Point(x,len([k for k in l if k<= x])))

    for i,P in enumerate(points[:-1]):
        N=points[i+1]
        Q=Point(N.x,P.y)
        segment1=Segment(P,Q)
        segment2=Segment(Q,N)
        segment1.parameters.color="blue"
        segment2.parameters.color=segment1.parameters.color
        segment2.parameters.style="dashed"
        pspict.DrawGraphs(segment1,segment2)


    pspict.grid.main_horizontal.parameters.style = "dotted"
    pspict.grid.main_vertical.parameters.style = "dotted"
    pspict.grid.num_subX=0
    pspict.grid.num_subY=0
    pspict.DrawGraphs(points)

    pspict.axes.do_mx_enlarge=False
    pspict.axes.do_my_enlarge=False
    pspict.axes.Dx=2
    pspict.axes.Dy=2
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()

