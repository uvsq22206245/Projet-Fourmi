# Projet de Fourmi de Langton
# Source : (http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)
# La fourmi de Langton - Documentation

from tkinter import *

COTE = 600                          
LARGEUR = COTE
HAUTEUR = COTE
UNITE = COTE // 7
LARGEUR_FLECHE = UNITE // 8
DELAI = 500

COULEUR_GRILLE = "gray30"
COULEUR_1 = 'black'
COULEUR_2 = 'white'

def dessine_fourmi(i, j, direction):                
    séparation = UNITE // 8
    est = (séparation, UNITE // 2)
    ouest = (UNITE - séparation, UNITE // 2)
    nord = (UNITE // 2, séparation)
    sud = (UNITE // 2, UNITE - séparation)
    x, y = j * UNITE, i * UNITE
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
        width=LARGEUR_FLECHE,
        arrow='last',
        fill='red',
        arrowshape=(18, 30, 8))

def dessine_carre(i, j):                                                  
    x, y = j * UNITE, i * UNITE
    carre = cnv.create_rectangle((x, y), (x + UNITE, y + UNITE),
                                  fill=COULEUR_1,
                                  outline='')
    cnv.tag_lower(carre)
    return carre

def dessin(position, direction, fourmi):                           
    cnv.delete(fourmi)
    (ii, jj), nouvelle_direction = bouger(position, direction, items)
    i, j = position
    carre = items[i][j]

    if carre == 0:
        carre = dessine_carre(i, j)
        items[i][j] = carre
    else:
        cnv.delete(carre)
        items[i][j] = 0

    nouvelle_fleche = dessine_fourmi(ii, jj, nouvelle_direction)
    return (ii, jj), nouvelle_direction, nouvelle_fleche

def bouger(position, direction, items):                             
    i, j = position
    a, b = direction
    aa, bb = (b, -a) if items[i][j] == 0 else (-b, a)

    newi, newj = i + aa, j + bb

    newi = newi % nouvelle_hauteur
    newj = newj % nouvelle_largeur

    return (newi, newj), (aa, bb)

def animation():                                                                 
    global position, direction, fourmi, id_anim, stop
    if not stop:
        position, direction, fourmi = dessin(position, direction, fourmi)
    id_anim = cnv.after(DELAI, animation)

root = Tk()                                             
cnv = Canvas(root, width=LARGEUR, height=HAUTEUR, background=COULEUR_2)
cnv.pack()

nouvelle_largeur = LARGEUR // UNITE                                                        
nouvelle_hauteur = HAUTEUR // UNITE

def faire_grille():                                                                
    for i in range(nouvelle_largeur):
        cnv.create_line((i * UNITE, 0), (i * UNITE, HAUTEUR), fill=COULEUR_GRILLE)
    for i in range(nouvelle_hauteur):
        cnv.create_line((0, i * UNITE), (LARGEUR, i * UNITE), fill=COULEUR_GRILLE)

def initialisation():                                                            
    global items, position, direction, fourmi, stop
    cnv.delete("all")
    cnv.focus_set()
    faire_grille()

    items = [[0] * nouvelle_largeur for _ in range(nouvelle_hauteur)]
    position = (nouvelle_hauteur // 2, nouvelle_largeur // 2)
    direction = (0, 1)
    fourmi = dessine_fourmi(position[0], position[1], direction)
    stop = True
    animation()

def on_off():                           
    global stop
    stop = not stop

def réinitialisation():                            
    cnv.after_cancel(id_anim)
    initialisation()

def étape_par_étape():                                                     
    global position, direction, fourmi, id_anim, stop
    if stop:
        position, direction, fourmi = dessin(position, direction, fourmi)

def accélerer():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = DELAI - 100

def ralentir():                                                 
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = DELAI + 100

def Lent():                                                    
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = 2000

def Normal():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = 500

def Rapide():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = 100

def Très_Rapide():                                            
    global position, direction, fourmi, id_anim, stop, DELAI
    DELAI = 15   

button1 = Button(root, text="On/Off", command=on_off)         
button1.pack(side=LEFT, padx=5, pady=5)

button2 = Button(root, text="Réinitialisation", command=réinitialisation)            
button2.pack(side=LEFT, padx=5, pady=5)

button3 = Button(root, text="Etape par étape", command=étape_par_étape)        
button3.pack(side=LEFT, padx=5, pady=5)

button4 = Button(root, text="<<", command=ralentir)                 
button4.pack(side=LEFT, padx=5, pady=5)

button5 = Button(root, text=">>", command=accélerer)              
button5.pack(side=LEFT, padx=5, pady=5)

button6 = Button(root, text="Lent", command=Lent)           
button6.pack(side=LEFT, padx=5, pady=5)

button7 = Button(root, text="Normal", command=Normal)          
button7.pack(side=LEFT, padx=5, pady=5)

button8 = Button(root, text="Rapide", command=Rapide)          
button8.pack(side=LEFT, padx=5, pady=5)

button9 = Button(root, text="Très Rapide", command=Très_Rapide)     
button9.pack(side=LEFT, padx=5, pady=5)

button10= Button(root, text="Revenir en arriere", command=revenir_en_arriere)
button10.pack(side=LEFT, padx=5, pady=5)

def revenirenarriere():
    L=[]
    L.append(fct ou se trouve la fourmi)
    pour supprimer(voir cours)
    (faire_grille)
    global fourmi_rang, fourmi_colonne, direction, previous_steps
    if any(previous_steps):
        row,col,previous_dir,color=previous_steps.pop()
        grid[rang][colonne] = color
        direction = previous_dir
        ant_colonne=rang
        ant_colonne= colonne
    print(previous_steps)
    drawgrid()

initialisation()
root.mainloop()
