from phystricks import *

def DS_statistics(moustaches,pspict):
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    #for i,m in enumerate(moustaches) :
    #    m.delta_y=0.75+i
    #    m.put_mark(0.2,0,"DS {}".format( len(moustaches)-i ),automatic_place=(pspict,"W"))
    for i,m in enumerate(moustaches) :
        m.delta_y=len(moustaches)+0.75-i-1
        m.put_mark(0.2,0,"DS {}".format( i+1 ),automatic_place=(pspict,"W"))

    maxy=len(moustaches)
    ledix=Segment(  Point(10,0),Point(10,maxy)   )
    ledix.parameters.color="green"
    ledix.parameters.linewidth=2
    ledix.parameters.style="dashed"

    pspict.DrawGraphs(moustaches,ledix)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
