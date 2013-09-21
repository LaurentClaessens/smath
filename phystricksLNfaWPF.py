# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

def LNfaWPF():
    pspict,fig = SinglePicture("LNfaWPF")
    pspict.dilatation(1)


    # Ici il suffit de mettre la grille avec les nombres de 1 à 9.
    # La substitution avec les nombres de -4 à 4 se fait automatiquement.
    tableau="""
.,.,.,.,i,.,i,i,5
i,6,.,5,2,.,i,.,.
.,.,2,.,.,3,4,i,.
4,2,.,.,i,i,i,.,7
i,.,.,.,6,.,i,.,.
.,.,1,.,.,5,.,.,.
2,.,i,i,5,.,6,.,i
i,.,.,.,1,.,7,.,i
i,4,.,.,3,.,i,.,.
"""
    solution="""
7,1,3,6,9,4,8,2,5
9,6,4,5,2,8,1,7,3
5,8,2,1,7,3,4,9,6
4,2,6,9,8,1,3,5,7
8,9,5,3,6,7,2,4,1
3,7,1,2,4,5,9,6,8
2,3,7,8,5,9,6,1,4
6,5,8,4,1,2,7,3,9
1,4,9,7,3,6,5,8,2
"""

    solution_substitution="""
2,-4,-2,  1,4,-1   ,3,-3,0
4,1,-1,   0,-3,3,   -4,2,-2
0,3,-3,  -4,2,-2,   -1,4,1

-1,-3,1   ,4,3,-4,   -2,0,2
3,4,0,    -2,1,2,   -3,-1,-4
-2,2,-4,  -3,-1,0    ,4,1,3

-3,-2,2    ,3,0,4    ,1,-4,-1
1,0,3,    -1,-4,-3   ,2,-2,4
-4,-1,4,   2,-2,1     ,0,3,-3
"""

    sudoku=SudokuGrid(tableau,length=0.7)

    pspict.DrawGraphs(sudoku)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

