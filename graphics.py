from turtle import *
from math import *
import time

currentL = None

COL = -1
ROW = -1

currentXs = []
currentYs = []

clrD = { 0:"white", 1:"red", 2:"blue", 3:"green", 4:"gold" , 5:"cyan", 6:"orange"}

global current_pos 
current_pos = (0.0,0.0)

def getPos(mouse_x, mouse_y):
    """Returns the row and column clicked by the mouse in a tuple."""
    global currentXs;
    global currentYs;
    global COL
    global ROW

    COL = 0
    ROW = 0
    
    for i in range(len(currentXs)-1):
        if currentXs[i] <= mouse_x < currentXs[i+1]:
            COL = i
    for i in range(len(currentYs)-1):
        if currentYs[i] <= mouse_y < currentYs[i-1]:
            ROW = i-1

    if mouse_x > 0 and COL == 0:
        COL = len(currentXs) - 2
    if mouse_y < 0 and ROW == 0:
        ROW = len(currentYs) - 2
        
    return (ROW, COL)

def setColor( key, color ):
    global clrD
    clrD[key] = color
    return

def colorLookup( clr ):
    global clrD
    if clr in clrD:
        return clrD[clr]
    else:
        return clr

def drawPolygon(polygon, cell_x, cell_y):
    print("drawing polygon!")
    x_start = polygon.x_offset + cell_x
    y_start = polygon.y_offset + cell_y
    x_start = x_start * polygon.length
    y_start = y_start * polygon.length
    delay(0)
    tracer(False)
    up()
    pencolor( "black" )
    clr = polygon.color
    clr = colorLookup( clr )
    try:
        fillcolor( clr )
    except:
        print("Color", clr, "was not recognized.")
        print("Using blue instead.")
        fillcolor( "blue" )
    goto(x_start, y_start)
    down()
    seth( 0 )
    right(polygon.offset_rotation)
    print("ok actually drawing now!")
    if polygon.value == 1:
        begin(fill)
        for s in range(polygon.sides):
            forward(polygon.length)
            right(polygon.angle)
        end(fill)
    else:
        for s in range(polygon.sides):
            forward(polygon.length)
            right(polygon.angle)
    up()

def drawCell(UnitCell):
    drawPolygon(UnitCell.d1, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s1, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s2, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s3, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s4, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s5, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.s6, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.h1, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.h2, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.h3, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.t1, UnitCell.x, UnitCell.y)
    drawPolygon(UnitCell.t2, UnitCell.x, UnitCell.y)

def drawUnitGrid(UnitGrid):
    for grid_col in UnitGrid.grid:
        for UnitCell in grid_col:
            drawCell(UnitCell)
    done()

def lifeMouseHandler(x,y):
    """ This function is called with each mouse click.

        Its inputs are the pixel location of the
        next mouse click: (x,y)
        
        It computes the column and row (within the board)
        where the click occurred with getPos, and changes the
        color of the clicked square.

        The overall list is shared between turtle graphics
        and the other parts of your program as a global
        variable named currentL. In general, global variables
        make software more complex, but sometimes they are
        necessary.
    """
    getPos(x,y) #update the position
    if ROW == 0 or ROW == len(currentL)-1 or COL == 0 or COL == len(currentL[0])-1:
        print("Don't click on the border!!! >:O")
    else: currentL[ROW][COL] = 1 - currentL[ROW][COL] 
    show(currentL)
    