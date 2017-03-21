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
    if polygon.value == 1:
        begin_fill()
        for s in range(polygon.sides):
            forward(polygon.length)
            right(polygon.angle)
        end_fill()
    else:
        for s in range(polygon.sides):
            forward(polygon.length)
            right(polygon.angle)
    up()

def drawCell(UnitCell):
    drawPolygon(UnitCell.d1, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s1, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s2, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s3, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s4, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s5, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.s6, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.t1, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.t2, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.h1, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.h2, UnitCell.draw_x, UnitCell.draw_y)
    drawPolygon(UnitCell.h3, UnitCell.draw_x, UnitCell.draw_y)


def drawUnitGrid(UnitGrid):
    for grid_col in UnitGrid.grid:
        for UnitCell in grid_col:
            drawCell(UnitCell)
    done()

#to write: mouse handler that finds what polygon the mouse click corresponds to 