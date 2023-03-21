# Projet de Fourmi de Langton
# Source : (http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)
# La fourmi de Langton - Documentation
# Partie 1

from tkinter import *

DIMENSION = 700
LARGEUR = DIMENSION
HAUTEUR = DIMENSION
UNIT = DIMENSION // 7
LARGEUR_FLECHE = UNIT // 8
DELAY = 500

COLOR_GRID = "black"
COLOR_ON = 'gray30'
COLOR_OFF = 'White'

def draw_fleche(i, j, drn):
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
        LARGEUR = LARGEUR_FLECHE,
        FLECHE = 'last',
        fill = 'red',
        FORME_FLECHE = (18, 30, 8))

#---------------------------------------------------------

# PARTIE 2
# Source : La fourmi de Langton - Documentation

#cette fonction permet de dessiner la carré
def draw_carre(i, j) :
    x, y = j * UNIT, i * UNIT
    CARRE = cnv.create_square((x, y), (x + UNIT, y + UNIT), fill = COLOR_ON, outline = '')
    cnv.tag_lower(CARRE)
    return CARRE

def draw(pos, drn, FLECHE) :
    cnv.delete(FLECHE)
    (ii, jj), ndrn = bouger(pos, drn, items)
    i, j = pos
    CARRE = items[i][j]

    if CARRE == 0 :
        CARRE = draw_carre(i, j)
        items[i][j] = CARRE
    else :
        cnv.delete(CARRE)
        items[i][j] = 0
    
    new_arrow = draw_fleche(ii, jj, ndrn)
    return(ii, jj), ndrn, new_arrow

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
root= Tk()  #importation bibliotheque creer une nouvelle fenetre ou on peut mettre le jeu
cnv= Canvas(root, LARGEUR=WIDTH, HAUTEUR= HEIGHT, background=COLOR_OFF) # cnv = esthetique
cnv.pack(side=CENTER) #ca sert a faire un pack ou on va mettre de nouvelle donne

new_largeur= LARGEUR // UNIT # diviser grille total paar les cases pour avoir la creation de petites cases
new_hauteur= HAUTEUR // UNIT # same thing but for hauteur

def make_grid():                #fct pour faire grille et ses dimensions
    for i in range(new_largeur):
        cnv.create_line(( i * UNIT, 0),
    for i in range(new_hauteur):
        cnv.create_line((0, i * UNIT),


def init():                      #initialiser, creer le tableau
    global items, pos, drn, arr, stop #la fonctio est la meme utise inside et outside la fonction
    cnv.delete("all")
    cnv.focus_set() #ce concentrer sur mouvemen de la fleche
    make_grid()
    items = [[0] * new_largeur for _ in range(new_hauteur)]                                      #pour qu on cree le tbaleau vide avec la fourmi au milieu 
    pos = (new_hauteur // 2, new_largeur // 2) # pour etre au centre du carre
    drn = (1,0)
    arr = draw_fleche(pos[0], pos[1], drn)
    stop = True # pour qu on commence pas l'animation
    anim()
                        
def on_off(event):        #evenement on off pour pauser ou continuer le jeu
    global stop
    stop = not stop
                        
def again(event): # evenement pour repetter le jeu depuis le debut
    cnv.after_cancel(id_anim)
    init()
                        
cnv.bind("<space>", on_off)
cnv.bind("<Escape>", again)
                        
init()
root.mainloop() # to do a loop so the game wont stop unless we say so
                        
