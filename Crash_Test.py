from CONFIGS import fichier_objets

x =['indice3 = [4, 5, 6]', "indice1 = {3: 'A B C'}"]

def objets_trouvés(x):
    if x in fichier_objets:
        return True
    else:
        return False
