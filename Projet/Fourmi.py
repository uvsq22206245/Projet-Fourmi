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
    est = (sep, UNIT // 2)
    ouest = (UNIT - sep, UNIT // 2)
    nord = (UNIT // 2, sep)
    sud = (UNIT // 2, UNIT - sep)
    x, y = j * UNIT, i * UNIT
    if direction == (0, 1):
        A = (x + est[0], y + est[1])
        B = (x + ouest[0], y + ouest[1])
    elif direction ==  (-1, 0):
        A = (x + sud[0], y + sud[1])
        B = (x + nord[0], y + nord[1])
    elif direction ==  (0, -1):
        B = (x + est[0], y + est[1])
        A = (x + ouest[0], y + ouest[1])
    else:
        B = (x + sud[0], y + sud[1])
        A = (x + nord[0], y + nord[1])
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

def on_off():
    global stop
    stop = not stop

def again():
    cnv.after_cancel(id_anim)
    init()

def step_by_step():
    global position, direction, arrow, id_anim, stop
    if stop:
        position, directionn, arrow = draw(position, direction, arrow)
         
         
button1 = Button(root, text="On/Off", command=on_off)
button1.pack(side=LEFT, padx=5, pady=5)

button2 = Button(root, text="Again", command=again)
button2.pack(side=LEFT, padx=5, pady=5)

button3 = Button(root, text="Step-by-Step", command=step_by_step)
button3.pack(side=LEFT, padx=5, pady=5)


init()
root.mainloop()
