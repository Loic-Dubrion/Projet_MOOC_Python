""" Projet d'évaluation de fin de session MOOC-Python 2022
    Auteur : DUBRION Loïc
    Date : 01/11/2022
    Jeu de type escape game"""

import turtle
from turtle import *
import CONFIGS

""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~ PROJET MOOC PYTHON ~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~ LANCELOT ET LE CHATEAU DU PYTHON NEIGES ~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

""" ***************  DEFINITIONS DES FONCTIONS  *************** 
    ****************  CONSTRUCTION DU CHATEAU *****************"""
def carre_optimal(a, b):    # Fonction permettant de calculer la taille optimale des cases
    h_max = c / b           # a = nb de colonnes
    l_max = d / a           # b = nb de lignes
    if h_max >= l_max:
        res = l_max
    else:
        res = h_max
    return res

def para_map(nb_ligne):     # Calcul le point de départ pour Turtle
    y = -240 + (h_carre * nb_ligne)     # Départ en haut à gauche
    return y

def trace_map(x, y):            # Dessine la carte de jeu
    turtle.tracer(False)        # Permet un affichage instantané
    zone_affichage()                # Definition de la zone d'affichage
    zone_inventaire()               # Definition de la zone d'inventaire
    goto(x, y)
    for z in range(27):         # Création des lignes
        for i in range(19):     # Création des colonnes
            matrice[z, i] = ((x + (0.5*h_carre), y - (0.5*h_carre)), trace_carre(plan[z][i]))
            x += h_carre
            goto(x, y)          # On décale le pointeur pour le carré suivant
        x = depart_x
        y -= h_carre
        goto(x, y)      # Point de départ pour la ligne suivante
    turtle.update()

def trace_carre(couleur):       # Dessine une case du jeu avec Turtle
    down()
    couleur_case = case_color(couleur)  # Renvoie à la fonction case_color
    color(couleur_case)
    begin_fill()
    for i in range(4):
        forward(h_carre)
        right(90)
    end_fill()
    up()
    return couleur

def case_color(x):      # Convertis le plan en couleur
    z = int(x)          # Convertis le paramètre reçu en number
    couleur_case = CONFIGS.COULEURS[z]      # Cherche la couleur via le fichier configs
    return couleur_case     # Retourne la couleur

def zone_affichage():       # Positionnement d'une 2nd tortue pour la zonne d'affichage
    turtle2.up()
    turtle2.goto(CONFIGS.POINT_AFFICHAGE_ANNONCES)
    turtle2.write("Bienvenue au château du Python des neiges", font=("Arial", 16, "bold"))


def zone_inventaire():      # Positionnement d'une 3ème tortue pour la zonne d'inventaire
    turtle3.up()
    turtle3.goto(CONFIGS.POINT_AFFICHAGE_INVENTAIRE)
    turtle3.write("INVENTAIRE :", font=("Arial", 14, "bold"))


""" ********************  CODE PRINCIPAL  ********************* 
    ****************  CONSTRUCTION DU CHATEAU *****************"""


grille_map = []     # Liste de tuples ((ligne, colonne), type de case)
setup(800, 600)     # Cadre du jeu
title("Lancelot et le château du Python des neiges")    # Titre de la fenêtre
turtle2 = Turtle()  # Création d'une 2nd tortue pour la zone d'affichage
turtle3 = Turtle()  # Création d'une 3ème tortue pour la zone d'inventaire
turtle.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()
up()

c = 440  # hauteur max
d = 290  # largeur max
depart_x = -240  # point de départ min

matrice = {}    # d'un dictionnaire { position du joueur : (coordonnées du joueur), type de case}
plan = []                                   # Liste recevant le plan du château

for line in open(CONFIGS.fichier_plan):     # Conversion du plan en liste
    line = line.rstrip('\n')
    line = line.split(" ")
    plan += [line]

h_carre = carre_optimal(19, 27)   # Dimension des cases
depart_y = para_map(27)          # Lieu de pose de la première case

trace_map(depart_x, depart_y)   # Lancement de la construction

""" ***************  DEFINITIONS DES FONCTIONS  *************** 
    *********************  PHASE DE JEU ***********************"""

""" Fonctions de déplacements """

def ecoute_active():    # Déclenche l’écoute du clavier
    turtle.listen()
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")
    turtle.onkeypress(deplacer_gauche, "Left")
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur

def deplacer_haut():                          # Fonction en réaction à up
    global coordonnees_player                 # Récupère la variable coordonnees_player
    turtle.onkeypress(None, "Up")             # Désactive la touche Left
    x = coordonnees_player[0] - 1             # Calcul des nouvelles coordonnées
    y = coordonnees_player[1]
    if (x, y) in matrice:                     # Test si les nouvelles coordonnées sont dans l'air de jeu
        deplacement(x, y)                     # Déclenche la fonction déplacement
    turtle.onkeypress(deplacer_haut, "Up")    # Réactive l'écoute des touches

def deplacer_bas():                           # Idem
    turtle.onkeypress(None, "Down")
    global coordonnees_player
    x = coordonnees_player[0] + 1
    y = coordonnees_player[1]
    if (x, y) in matrice:
        deplacement(x, y)
    turtle.onkeypress(deplacer_bas, "Down")

def deplacer_gauche():
    turtle.onkeypress(None, "Left")           # Idem
    global coordonnees_player
    x = coordonnees_player[0]
    y = coordonnees_player[1] - 1
    if (x, y) in matrice:
        deplacement(x, y)
    turtle.onkeypress(deplacer_gauche, "Left")

def deplacer_droite():
    turtle.onkeypress(None, "Right")            # Idem
    global coordonnees_player
    x = coordonnees_player[0]
    y = coordonnees_player[1] + 1
    if (x, y) in matrice:
        deplacement(x, y)
    turtle.onkeypress(deplacer_droite, "Right")

def deplacement(x, y):                          # Déplace le joueur
    global coordonnees_player
    if matrice[(x, y)][1] == "0":               # Couloir, on avance
        turtle_player.goto(matrice[(x, y)][0])  # Déplace la tortue
        new_point()                             # Déclenche la fonction qui dessine le nouveau point
        visit()                                 # Déclenche la fonction qui dessine les cases visitées
        coordonnees_player = (x, y)
        return coordonnees_player               # Retourne les nouvelles coordonnées
    if matrice[(x, y)][1] == "1":               # Mur, on renvoie la position
        return coordonnees_player
    if matrice[(x, y)][1] == "2":               # Sortie! on avance
        turtle_player.goto(matrice[(x, y)][0])  # Déplace la tortue
        new_point()                             # Déclenche la fonction qui dessine le nouveau point
        visit()                                 # Déclenche la fonction qui dessine les cases visitées
        coordonnees_player = (x, y)
        turtle2.clear()
        turtle2.write("Vous avez gagné !!!", font=("Arial", 16, "bold"))
    if matrice[(x, y)][1] == "3":               # Porte
        if porte(x, y):                         # Déclenchement de la fonction
            turtle_player.goto(matrice[(x, y)][0])  # Déplace la tortue
            new_point()
            visit()
            coordonnees_player = (x, y)
            ecoute_active()                         # Je réenclenche l'écoute
            return coordonnees_player               # Retourne les nouvelles coordonnées
    if matrice[(x, y)][1] == "4":               # Objet
        turtle_player.goto(matrice[(x, y)][0])  # Déplace la tortue
        new_point()  # Déclenche la fonction qui dessine le nouveau point
        visit()  # Déclenche la fonction qui dessine les cases visitées
        coordonnees_player = (x, y)
        indice(coordonnees_player)      # déclenchement de la fonction indice
        return coordonnees_player  # Retourne les nouvelles coordonnées
    ecoute_active()  # Je réenclenche l'écoute


def new_point():                                # Dessine la nouvelle position du joueur
    turtle_player.clear()
    turtle_player.down()
    turtle_player.dot((h_carre * CONFIGS.RATIO_PERSONNAGE), CONFIGS.COULEUR_PERSONNAGE)
    turtle_player.up()

def visit():                                    # Coloriage des cases visitées
    global coordonnees_player
    turtle.tracer(False)
    turtle.up()     # Je mets ma tortue en haut à gauche de la case
    x = matrice[coordonnees_player][0][0] - (0.5*h_carre)
    y = matrice[coordonnees_player][0][1] + (0.5*h_carre)
    turtle.goto(x, y)
    turtle.down()
    color(CONFIGS.COULEUR_VUE)
    begin_fill()
    for i in range(4):
        forward(h_carre)
        right(90)
    end_fill()
    up()
    turtle.update()


""" Fonctions de déclenchement d'action"""

def indice(x):              # Déclenchement de l'affichage indice
    global inventaire
    if x in inventaire:     # Vérifie si l'indice a déjà été donné
        return
    else:
        for ligne in open(CONFIGS.fichier_objets, encoding="UTF-8"):    # Récupère l'indice dans le fichier
            if str(x) in ligne:
                ligne_enigme = nettoyage_indice(ligne)  # Retourne une liste position / indice
                turtle3.goto(turtle3.pos()[0], turtle3.pos()[1] - 40)
                longueur = len(ligne_enigme[1])     # Coupe l'indice si celui-ci est trop long
                if longueur > 30:
                    turtle3.goto(turtle3.pos()[0], turtle3.pos()[1] - 20)
                    my_string = ligne_enigme[1]
                    split_strings = my_string.split()
                    split_strings.insert(5, '\n')
                    final_string = ' '.join(split_strings)
                    turtle3.write(final_string, font=("Arial", 14, "normal"))
                else:
                    turtle3.write(ligne_enigme[1], font=("Arial", 14, "normal"))   # Affiche l'indice
                inventaire.append(x)        # Enregistre le passage dans la liste inventaire
        return inventaire

def porte(x, y):       # Lancement de la fonction avec mes coordonnées en paramètre
    global coordonnees_player
    global deja_vu      # Je récupère ma liste
    if (x, y) in deja_vu:    # Je vérifie n'être jamais venu
        turtle_player.goto(matrice[(x, y)][0])  # Déplace la tortue
        new_point()
        visit()
        coordonnees_player = (x, y)
        return
    turtle2.clear()
    turtle2.write("Cette porte est fermée", font=("Arial", 16, "bold"))
    string_coor = "("+str(x)+", "+str(y)+")"        # Je converti mes x, y en string
    for ligne in open(CONFIGS.fichier_questions, encoding="UTF-8"):  # Récupère la question dans le fichier
        if str(string_coor) in ligne:        # Je cherche l'énigme correspondant à ma position
            ligne_enigme = nettoyage(ligne)         # Je nettoie mon fichier
            if ouverture_enigme(ligne_enigme[1], ligne_enigme[2]):  # Je lance mon enigme
                deja_vu.append((x, y))  # C'est juste. J'enregistre le passage dans ma liste
                return deja_vu      # Je retourne ma liste deja_vu & je continue
            else:
                return False            # Mauvaise réponse, retour au jeu

def nettoyage(x):       # Nettoyage du fichier, retourne une liste [position, question, réponse]
    ligne_enigme = x.replace("'", '"').split('"')
    for i in ligne_enigme:
        if len(i) < 3:
            ligne_enigme.remove(i)
    ligne_enigme[0] = ligne_enigme[0][0:-3]
    if len(ligne_enigme) > 3:
        ligne_enigme[1] = ligne_enigme[1] + "'" + ligne_enigme[2]
        ligne_enigme.remove(ligne_enigme[2])
    return ligne_enigme

def ouverture_enigme(question, reponse):    # Retourne un booléen
    reponse_player = turtle.textinput("enigme", question)
    if reponse_player == reponse:
        turtle2.clear()
        turtle2.write("Bravo ! Vous êtes passé!", font=("Arial", 16, "bold"))
        res = True
    else:
        turtle2.clear()
        turtle2.write("Perdu ! Essaie encore!", font=("Arial", 16, "bold"))
        res = False
    return res

def nettoyage_indice(x):
    ligne_enigme1 = x.split('"')
    ligne_enigme2 = x.split("'")
    if len(ligne_enigme1[0]) > len(ligne_enigme2[0]):
        ligne_enigme = ligne_enigme2
    else:
        ligne_enigme = ligne_enigme1
    for i in ligne_enigme:
        if len(i) < 3:
            ligne_enigme.remove(i)
    ligne_enigme[0] = ligne_enigme[0][0:-2]
    return ligne_enigme


""" ************************************************
    ***************  CODE PRINCIPAL  *************** 
    ************************************************ 
    ****************  PHASE DE JEU *****************
    ************************************************"""

""" Configuration de la tortue joueur"""

coordonnees_player = CONFIGS.POSITION_DEPART            # Variable global position joueur
inventaire = []          # Liste les objets trouvés
deja_vu = []
turtle_player = Turtle()                                # Nouvelle tortue position joueur
turtle_player.hideturtle()
turtle_player.up()
turtle_player.goto(matrice[CONFIGS.POSITION_DEPART][0])     # Positionnement du joueur
turtle_player.dot((h_carre * CONFIGS.RATIO_PERSONNAGE), CONFIGS.COULEUR_PERSONNAGE)   # Paramètre visuel
turtle_player.up()

ecoute_active()

exitonclick()
