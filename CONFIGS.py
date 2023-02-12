ZONE_PLAN_MINI = (-240, -240)  # Coin inférieur gauche de la zone d'affichage du plan
ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
POINT_AFFICHAGE_ANNONCES = (-240, 210)  # Point d'origine de l'affichage des annonces
POINT_AFFICHAGE_INVENTAIRE = (70, 150)  # Point d'origine de l'affichage de l'inventaire

# Les valeurs ci-dessous définissent les couleurs des cases du plan
COULEUR_CASES = 'white'     # 0
COULEUR_COULOIR = 'white'   # 0
COULEUR_MUR = 'grey'        # 1
COULEUR_OBJECTIF = 'yellow' # 2
COULEUR_PORTE = 'orange'    # 3
COULEUR_OBJET = 'green'     # 4
COULEUR_VUE = 'wheat'       # 5
COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, COULEUR_OBJET, COULEUR_VUE]
COULEUR_EXTERIEUR = 'white'

# Couleur et dimension du personnage
COULEUR_PERSONNAGE = 'red'
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 1)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_plan = 'plan_chateau.txt'
fichier_questions = 'dico_portes.txt'
fichier_objets = 'dico_objets.txt'
