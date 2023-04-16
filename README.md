# Projet-Fourmi
---

#  Groupe BI-TD3
* NAHAS Samer
* SOULEYMANE Haoua
* SIVANESAN Aginthan

# URL de dépôt
* https://github.com/uvsq22206245/Projet-Fourmi

# Documentation du projet

* Règles de la fourmi
 
Il y a une fourmi au centre de la grille, quand elle est sur une case blanche elle va sur la case à sa droite. Et la case où la fourmi était devient noire. Dans le cas où la fourmi aurait été sur une case noire, elle serait aller sur la case à sa gauche, et l'ancienne case où elle se trouvait deviendrait blanche.

* Explications du programme

.En premier nous avons importer la bibliothèque Tkinter car avec celle-ci on peut créer une interface graphique.
Nous avons définis des variables tel que la hauteur, largeur de la grille. Des variables "couleur_1" et "couleur_2" qui seront les couleurs des états des cases où la fourmi passe, c'est-à-dire blanc et noir.
Nous avons défini en premier la fonction "dessine_fourmi". Cette fonction permet de dessiner un fourmi en prenant en compte la distance en la tête de la flèche et la case et la queue de la flèche et la case. Nous avons défini des variables ( est, nord, ouest, sud) qui pourront nous aider à connaître l'orientation de la flèche afin de connaître sa gauche et sa droite et donc de savoir vers où elle ira et en quelle couleur deviendra la case où elle se trouvait.
La fonction "dessine_carre" permet de créer les case de la grille mais également de changer les couleurs. 
La fonction "dessin" est une fonction réunissant les fonctions "dessine_carre" et "dessine_fourmi". Avec cette fonction permet de dessiner la fourmi sur la case où elle doit aller et de "dessiner" la nouvelle case avec son changement de couleur. Dans cette fonction nous avons utiliser une fonction qui s'appelle "bouger". Cette dernière permet selon les coordonnées de la flèche de prédire la nouvelle position de la fourmi ansi que l'orientatien de celle-ci (la fourmi est la flèche).
C'est également dans cette fonction dque nous avons établis le tore.
Cette fonction nous pemret l'animation de la fourmi sans avoir à appuyer sur un bouton. Elle se déplace selon un délais précis.
La fonction "faire_grille" permet d'assambler toutes les cases ensemble, elle divise la grande case en sous-cases.
La fonction "initialisation" nous permet de donner une position de départ à notre fourmi, en l'occurence c'est le milieu de la grille.
