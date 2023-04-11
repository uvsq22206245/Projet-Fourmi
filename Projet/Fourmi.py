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

COLOR_GRID = "gray30"
COLOR_ON = 'black'
COLOR_OFF = 'white'

def draw_arrow(i, j, direction):
    sep = UNIT // 8
    east = (sep, UNIT // 2)
    west = (UNIT - sep, UNIT // 2)
    north = (UNIT // 2, sep)
    south = (UNIT // 2, UNIT - sep)
    x, y = j * UNIT, i * UNIT
    if direction == (0, 1):
        A = (x + east[0], y + east[1])
        B = (x + west[0], y + west[1])
    elif direction ==  (-1, 0):
        A = (x + south[0], y + south[1])
        B = (x + north[0], y + north[1])
    elif direction ==  (0, -1):
        B = (x + east[0], y + east[1])
        A = (x + west[0], y + west[1])
    else:
        B = (x + south[0], y + south[1])
        A = (x + north[0], y + north[1])
    return cnv.create_line(
        A,
        B,
        width=ARROW_WIDTH,
        arrow='last',
        fill='red',
        arrowshape=(18, 30, 8))


def draw_square(i, j):
    x, y = j * UNIT, i * UNIT
    square = cnv.create_rectangle((x, y), (x + UNIT, y + UNIT),
                                  fill=COLOR_ON,
                                  outline='')
    cnv.tag_lower(square)
    return square


def draw(position, direction, arrow):
    cnv.delete(arrow)
    (ii, jj), newdirection = bouger(position, direction, items)
    i, j = position
    square = items[i][j]

    if square == 0:
        square = draw_square(i, j)
        items[i][j] = square
    else:
        cnv.delete(square)
        items[i][j] = 0

    newarrow = draw_arrow(ii, jj, newdirection)
    return (ii, jj), newdirection, newarrow

def bouger(position, direction, items):
    i, j = position
    a, b = direction
    aa, bb = (b, -a) if items[i][j] == 0 else (-b, a)

    newi, newj = i + aa, j + bb

    newi = newi % newheight
    newj = newj % newwidth

    return (newi, newj), (aa, bb)

def anim():
    global position, direction, arrow, id_anim, stop
    if not stop:
        position, direction, arrow = draw(position, direction, arrow)
    id_anim = cnv.after(DELAY, anim)

root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, background=COLOR_OFF)
cnv.pack()

newwidth = WIDTH // UNIT
newheight = HEIGHT // UNIT

def make_grid():
    for i in range(newwidth):
        cnv.create_line((i * UNIT, 0), (i * UNIT, HEIGHT), fill=COLOR_GRID)
    for i in range(newheight):
        cnv.create_line((0, i * UNIT), (WIDTH, i * UNIT), fill=COLOR_GRID)


def init():
    global items, position, direction, arrow, stop
    cnv.delete("all")
    cnv.focus_set()
    make_grid()

    items = [[0] * newwidth for _ in range(newheight)]
    position = (newheight // 2, newwidth // 2)
    direction = (0, 1)
    arrow = draw_arrow(position[0], position[1], direction)
    stop = True
    anim()

def on_off(event):
    global stop
    stop = not stop

def again(event):
    cnv.after_cancel(id_anim)
    init()

def step_by_step(event):
    global position, direction, arrow, id_anim, stop
    if stop:
        position, directionn, arrow = draw(pos, drn, arr)

cnv.bind("<space>", on_off)
cnv.bind("<Escape>", again)
cnv.bind("<Right>", step_by_step)

init()
root.mainloop()
