from puissance_4_modules import *

lnom = saisir_nom_2_joueurs()
init_score = init_scores_joueur_actif()
while True:
    joueur_actif = 0
    grille = init_grille()
    while True:
        afficher_grille(grille)
        colonne = saisir_colonne_joueur_actif(lnom[joueur_actif])
        if 0 <= colonne < 7 and grille[0][colonne] == " ":
            grille = mette_a_jour_grille(grille, colonne, joueur_actif)
            ok = partie_finie(grille, joueur_actif)
            if ok == 1:
                afficher_grille(grille)
                mettre_a_jour_score(init_score, joueur_actif)
                affiche_victoire(lnom[joueur_actif])
                break
            elif ok == 2:
                afficher_grille(grille)
                afficher_pat()
                break
            elif ok == 0:
                joueur_actif = changer_joueur_actif(joueur_actif)
        else:
            print("Mauvaise colonne.")
    afficher_scores(lnom,init_score)
    choix = int(input("1) Nouvelle partie \n2) Sortie \nSaisissez un nombre : "))
    if choix == 1:
        continue
    else:
        print("Thank you for playing the game.")
        break
