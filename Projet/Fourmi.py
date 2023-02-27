#Projet de Fourmi de Langton
# PARTIE 2
# Source : La fourmi de Langton - Documentaion

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