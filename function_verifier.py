import pandas as pd
import function_tester_sandwich as fts
import Partie_init as init


def verifier_coup(df_jeu, lig, col, case, cas_passe="") : 
    
    # Teste le cas "Passe ton tour"
    if cas_passe == "passe": #on n'a besoin de vérifier que si le joueur veut passer son tour, les coordonnées entrées doivent être invalides
        flag_coup_ok = False
        # On vérifie qu'il n'y a pas de sandwich possible
        if fts.tester_sandwich_possible(df_jeu,case) == False:
            print("Passe ton tour - Pas de sandwich possible")
            return "passe"
            
    else:
        flag_coup_ok = True

    # Teste si les coordonnées en ligne et colonne sont sur l'échiquier
    if lig >9 or lig <1 :
        print("Erreur Numéro de ligne - Coup joué hors de l'échiquier")
        flag_coup_ok = False
    
    if flag_coup_ok == True and (col >9 or col <1) :
        print("Erreur Numéro de Colonne - Coup joué hors de l'échiquier")
        flag_coup_ok = False

    # Teste si la case est déjà jouée
    req = 'lig == ' + str(lig) + ' and col == ' + str(col)
    case_testee = df_jeu.query(req).iloc[0]["cases"]
    if flag_coup_ok == True and case_testee != "dispo" :
        print("Coup déjà joué")
        flag_coup_ok = False

    # teste si la case est voisine d'une case déjà jouée
    if flag_coup_ok == True and fts.est_case_adj_vide(df_jeu,lig,col) == True:
        print("case non voisine d'une case jouée")
        flag_coup_ok = False
    
    

    # Teste si la case jouée permet de faire un sandwich
    if flag_coup_ok != False and cas_passe != "passe" and fts.tester_sandwich(df_jeu, lig, col, case) == False :
        print("Il n' y a pas de sandwich pour ce coup")
        flag_coup_ok = False
  
    return flag_coup_ok

#print(verifier_coup(init.echiquier, 1,2,"noir","passe"))


