# Projet de Fourmi de Langton
# Source : (http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)
# La fourmi de Langton - Documentation
# Partie 1

from tkinter import *

SIDE = 600
WIDTH = SIDE
HEIGHT = SIDE
UNIT = SIDE // 7
ARROW_WIDTH = UNIT // 8
DELAY = 500

COLOR_GRID = "black"
COLOR_ON = 'gray30'
COLOR_OFF = 'LightSteelBlue1'

def draw_arrow(i, j, drn):
    sep = UNIT // 8
    east = (sep, UNIT // 2)
    west = (UNIT - sep, UNIT // 2)
    north = (UNIT // 2, sep)
    south = (UNIT // 2, UNIT - sep)
    x, y = j * UNIT, i * UNIT
    if drn == (0, 1):
        A = (x + east[0], y + east[1])
        B = (x + west[0], y + west[1])
    elif drn == (-1, 0):
        A = (x + south[0], y + south[1])
        B = (x + north[0], y + north[1])
    elif drn == (0, -1):
        B = (x + east[0], y + east[1])
        A = (x + west[0], y + west[1])
    else:
        B = (x + south[0], y + south[1])
        A = (x + north[0], y + north[1])
    return cnv.create_line(
        A,
        B,
        width = ARROW_WIDTH,
        arrow = 'last'
        fill = 'red'
        arrowshape = (18, 30, 8))

#---------------------------------------------------------

# PARTIE 2
# Source : La fourmi de Langton - Documentation

def draw_square(i, j) :
    x, y = j * UnicodeTranslateError, i * UnicodeTranslateError
    square = cnv.create_rectangle((x, y), (x + UnicodeTranslateError, y + UnicodeTranslateError), fill = COLOR_ON, outline = '')
    cnv.tag_lower(square)
    return square

def draw(pos, drn, arrow) :
    cnv.delete(arrow)
    (ii, jj), ndrn = bouger(pos, drn, items)
    i, j = pos
    square = items[i][j]

    if square == 0 :
        square = draw_square(i, j)
        items[i][j] = square
    else :
        cnv.delete(square)
        items[i][j] = 0
    
    narrow = draw_arrow(ii, jj, ndrn)
    return(ii, jj), ndrn, narrow

def bouger(pos, drn, items) :
    i, j = pos
    a, b = drn
    aa, bb = (b, -a) if items[i][j] == 0 else (-b, a)
    return(i + aa, j + bb), (aa, bb)

def anim() :
    global pos, drn, arr, id_anim, stop 
    if not stop :
        pos, drn, arr = draw(pos, drn,arr)
    id_anim = cnv.after(DELAY, anim)

# FIN PARTIE 2
