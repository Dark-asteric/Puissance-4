BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'
def saisir_nom_2_joueurs():
    noms = []
    noms.append(input("Entrer le nom du joueur 1 : "))
    noms.append(input("Entrer le nom du joueur 2 : "))
    return noms

def init_scores_joueur_actif():
    scores = [0,0]
    return scores

def init_grille():
    grille = [[" " for i in range(7)] for j in range(6)]
    return grille

def afficher_grille(grille):
    print("  0 1 2 3 4 5 6")
    i = 0
    for row in grille:
        print(i,end=" ")
        for item in row:
            # Apply color based on the content
            if "0" in item:
                print(BLUE + item + RESET, end=" ")
            elif "1" in item:
                print(YELLOW + item + RESET, end=" ")
            else:
                print(item, end=" ")
        print()
        i += 1
    """
    for row in grille:
        print(i, end=" ")
        print(" ".join(row))
        i += 1
    """
    """
    for row in grille:
        print(i,end="")
        for col in row:
            if '0' in col:
                print("\033[94m",col,"\033[0m",end="")
            elif '1' in col:
                print("\033[93m",col,"\033[0m",end = "")
            else:
                print(col,end=" ")
        print()
        i += 1
    """

def saisir_colonne_joueur_actif(nom_joueur_actif):
    col = int(input(f"{nom_joueur_actif} , saisissez la colonne où déposer un jeton (0 à 6) : "))
    return col

def mette_a_jour_grille(grille,colonne_joue,code_joueur_actif):
    #if 0<= colonne_joue < 7:
        for i in range(5,-1,-1):
            if grille[i][colonne_joue] == " ":
                grille[i][colonne_joue] = str(code_joueur_actif)
                break
        return grille

def partie_finie(grille,code_joueur_actif):
    for row in grille:
        for i in range(len(row) - 3):
            if all(cell == str(code_joueur_actif) for cell in row[i:i+4]):
                return True
    for col in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if all(grille[row][col] == str(code_joueur_actif) for row in range(i, i+4)):
                return True
    for row in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if all(grille[row+i][col+i] == str(code_joueur_actif) for i in range(4)):
                return True
    for row in range(len(grille) - 3):
        for col in range(3, len(grille[0])):
            if all(grille[row+i][col-i] == str(code_joueur_actif) for i in range(4)):
                return True
    return False

def changer_joueur_actif(code_joueur_actif):
    code_joueur_actif = (code_joueur_actif + 1)%2
    return code_joueur_actif

# lsocres table
def mettre_a_jour_score(lscore,code_joueur_actif):
    lscore[code_joueur_actif] += 1

# name
def affiche_victoire(nom_joueur_actif):
    print(f"{nom_joueur_actif}, vous avez gagné...")

def verifier_pat(grille):
    for row in grille:
        if " " in row:
            return False
    return True

def afficher_pat():
    print("La partie est pat.")

def afficher_scores(lnoms_joueur,lscores):
    print(f"{lnoms_joueur[0]}, votre score est de {lscores[0]}")
    print(f"{lnoms_joueur[1]}, votre score est de {lscores[1]}")

