# Projet de Fourmi de Langton
# Source : (http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)
# La fourmi de Langton - Documentation
#base: si la case est blanche la fourmiepasse vers la droite si la case est noir la fourmi passe vers la gauche
from tkinter import *

COTE = 600                          
LARGEUR = COTE
HAUTEUR = COTE
UNITE = COTE // 7
LARGEUR_FLECHE = UNITE // 8
DELAI = 500

COULEUR_GRILLE = "gray"
COULEUR_1 = 'black'
COULEUR_2 = 'white'

mouvements_precedents = []
# (i,j,direction): ordonne, abscisse,direction de la fleche)
# x= j*unite et y= i*unite
#unite+une case complette
def dessine_fourmi(i, j, direction):     # dessine la fourmi           
    séparation = UNITE // 8  #c'est la separation entre la grille et la fleche, ca controle la taille de la fleche UNIT= taille d une case
    est = (séparation, UNITE // 2) # pour centrer pour qu elle ne soit pas pencher
    ouest = (UNITE - séparation, UNITE // 2) 
    nord = (UNITE // 2, séparation)                         # on a utilise nord sud est et ouest pour pouvoir a la fin mettre la felche au centre de notre programme
    sud = (UNITE // 2, UNITE - séparation)
    x, y = j * UNITE, i * UNITE                     #[0] la ou la fleche ne pointe pas et [1] la ou la fleche pointe
    if direction == (0, 1):                          #coordonne pour que la fleche pointe vers la droite
        A = (x + est[0], y + est[1])                   
        B = (x + ouest[0], y + ouest[1])
    elif direction ==  (-1, 0):
        A = (x + sud[0], y + sud[1])
        B = (x + nord[0], y + nord[1])           # A c est pour le debut de la fleche (sa tete) et B c est la fin 
    elif direction ==  (0, -1):                  # cette fonction est utilise pour dessiner et centrer l emplacement de la fourmi
        B = (x + est[0], y + est[1])
        A = (x + ouest[0], y + ouest[1])
    else:
        B = (x + sud[0], y + sud[1])
        A = (x + nord[0], y + nord[1])
    return cnv.create_line(                 #ligne ou on remplie la fleche et son contour
        A,
        B,
        width=LARGEUR_FLECHE,
        arrow='last',
        fill='red',
        arrowshape=(18, 30, 8))

def dessine_carre(i, j):       #dessin les petites cases noires                                              
    x, y = j * UNITE, i * UNITE
    carre = cnv.create_rectangle((x, y), (x + UNITE, y + UNITE), #cnv = fct qui nous permet de creer la page
                                  fill=COULEUR_1, #colorier les carres
                                  outline='') #repassage du carre
    cnv.tag_lower(carre) #ca permet de bouger un objet
    return carre

def dessin(position, direction, fourmi):     # fct qui nous laisse "fusionner" les fourmi et les cases ensemble                      
    global mouvements_precedents             
    etat_case = items[position[0]][position[1]]  #enregistrer la position de la fourmi
    mouvements_precedents.append((position, direction, etat_case))
    cnv.delete(fourmi) 
    (ii, jj), nouvelle_direction = bouger(position, direction, items)
    i, j = position
    carre = items[i][j] #fct qui permet d'appeler un objet, items=grille

    if carre == 0:  #0 c'est la couleur blanche comme on a l'a definit avant, si le carre est blanc le carre va resevoir la fct dessine carre, et quand il est blanc il va devenir noir 
        carre = dessine_carre(i, j)
        items[i][j] = carre     #la grille recoit le carre mais d une couleur precise(soit noir soit blanc)
    else:
        cnv.delete(carre) #eneleve une case noir
        items[i][j] = 0  #definit la couleur blanche(change une case noir en blanc)

    nouvelle_fleche = dessine_fourmi(ii, jj, nouvelle_direction) #i pour la queue de la fourmi et le deuxieme pour la tete de la fourmi et meme chose pour j.
    return (ii, jj), nouvelle_direction, nouvelle_fleche

def bouger(position, direction, items):                             
    i, j = position
    a, b = direction
    aa, bb = (b, -a) if items[i][j] == 0 else (-b, a)

    newi, newj = i + aa, j + bb           #nouvelle position et nouvelle direction de la fourmi par rapport a son deplacement

    newi = newi % nouvelle_hauteur       # pour faire le tore= quand la fourmi depace la grille et elle revient de l autre cote, on calcule la nouvelle pos de la fourmi avec le modulo et si le modulo est egal a rien il va remettre de la autre cote
    newj = newj % nouvelle_largeur      #meme chose mais avec largeur

    return (newi, newj), (aa, bb)

def animation():                                                                 
    global position, direction, fourmi, id_anim, stop
    if not stop:                                                              
        position, direction, fourmi = dessin(position, direction, fourmi)
    id_anim = cnv.after(DELAI, animation)  #cnv.after ca sert a lancer l animation apres un ceratin delai.

root = Tk()        
root.title("Fourmi de Langton")  
root.geometry("1000x1000")                                         #esthetique
cnv = Canvas(root, width=LARGEUR, height=HAUTEUR, background=COULEUR_2)
cnv.pack()

nouvelle_largeur = LARGEUR // UNITE             #pour diviser la grille totale par des cases, pour pouvoir creer des petites cases                                          
nouvelle_hauteur = HAUTEUR // UNITE

def faire_grille():                                                                
    for i in range(nouvelle_largeur):
        cnv.create_line((i * UNITE, 0), (i * UNITE, HAUTEUR), fill=COULEUR_GRILLE)   #fonction qui nous aide a faire une grille et donc  tous les cases  doivent etre initialise en blanc
    for i in range(nouvelle_hauteur):                                                #
        cnv.create_line((0, i * UNITE), (LARGEUR, i * UNITE), fill=COULEUR_GRILLE)

def initialisation():                                                            
    global items, position, direction, fourmi, stop
    cnv.delete("all")
    cnv.focus_set()       #ce concentrer sur un widget sur un objet donc ce contrer sur la fleche
    faire_grille()

    items = [[0] * nouvelle_largeur for _ in range(nouvelle_hauteur)]
    position = (nouvelle_hauteur // 2, nouvelle_largeur // 2)               #on divise longueur et largeur par 2 pour que la flece soit au centre du carre 
    direction = (0, 1)
    fourmi = dessine_fourmi(position[0], position[1], direction)
    stop = True                                  # animation pas commence
    animation()

def on_off():                           
    global stop                    #animation commence ou non
    stop = not stop

def réinitialisation():                            
    cnv.after_cancel(id_anim)        #pour reinitialiser la fourmi
    initialisation()

def étape_par_étape():                                                     
    global position, direction, fourmi, id_anim, stop
    if stop:                                           #la fourmi marche etape par etape
        position, direction, fourmi = dessin(position, direction, fourmi)

def annuler():
    global position, direction, fourmi, id_anim, stop, items, mouvements_precedents
    if mouvements_precedents:
        dernier_mouvement = mouvements_precedents.pop()
        position, direction, etat_case = dernier_mouvement        #annuler des steps
        i, j = position
        if etat_case == 0:       #0 couleur blanche
            cnv.delete(items[i][j])         #pour supprimer(i,j) abscisse ordonne sur la case ou se trouve la fourmi
            items[i][j] = 1             # donc la case redevient noir si elle etait balnche quan don retourne en arriere
        else:
            items[i][j] = dessine_carre(i, j)
            cnv.delete(etat_case)
        cnv.delete(fourmi)
        nouvelle_fleche = dessine_fourmi(i, j, direction)
        fourmi = nouvelle_fleche
        
def accélerer():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI   # fct accelerer la fourmi graduellement
    DELAI = DELAI - 100

def ralentir():                                                 
    global position, direction, fourmi, id_anim, stop, DELAI   #fct ralentir la fourmi graduellement
    DELAI = DELAI + 100

def Lent():                                                    
    global position, direction, fourmi, id_anim, stop, DELAI #fct pour que la fourmi passe lentement
    DELAI = 2000

def Normal():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI #fct rapidite normal
    DELAI = 500

def Rapide():                                                  
    global position, direction, fourmi, id_anim, stop, DELAI   #fct fourmi rapide
    DELAI = 100

def Très_Rapide():                                            
    global position, direction, fourmi, id_anim, stop, DELAI  #fct tres rapide
    DELAI = 15   
#creation des boutons pour nos fct           
button1 = Button(root, text="On/Off", command=on_off)         
button1.pack(side=LEFT, padx=5, pady=5)           

button2 = Button(root, text="Réinitialisation", command=réinitialisation)            
button2.pack(side=LEFT, padx=5, pady=5)

button3 = Button(root, text="Etape par étape", command=étape_par_étape)        
button3.pack(side=LEFT, padx=5, pady=5)

button4 = Button(root, text="<<", command=ralentir)                 
button4.pack(side=LEFT, padx=5, pady=5)

button5 = Button(root, text=">>", command=accélerer)              
button5.pack(side=LEFT, padx=5, pady=5)                                    #padx et pady c est la distance entre les boutons x ordonne et y abscisse

button6 = Button(root, text="Lent", command=Lent)           
button6.pack(side=LEFT, padx=5, pady=5)

button7 = Button(root, text="Normal", command=Normal)          
button7.pack(side=LEFT, padx=5, pady=5)

button8 = Button(root, text="Rapide", command=Rapide)          
button8.pack(side=LEFT, padx=5, pady=5)

button9 = Button(root, text="Très Rapide", command=Très_Rapide)     
button9.pack(side=LEFT, padx=5, pady=5)

button10 = Button(root, text="Etape précédente", command=annuler)     
button10.pack(side=LEFT, padx=5, pady=5)

initialisation()
root.mainloop()               #pour pouvoir donc faire une boucle
