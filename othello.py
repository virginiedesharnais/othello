import pandas as pd

def verifier_coup(df_jeu, lig, col, case) : 
    flag_coup_ok = True
    
    # Teste si les coordonnées en ligne et colonne sont sur l'échiquier
    if lig >9 or lig <1 :
        print("Erreur Numéro de ligne - Coup joué hors de l'échiquier")
        flag_coup_ok = False
    
    if col >9 or col <1 :
        print("Erreur Numéro de Colonne - Coup joué hors de l'échiquier")
        flag_coup_ok = False

    # Teste si la case est déjà jouée
    req = 'lig == ' + str(lig) + ' and col == ' + str(col)
    case_testee = df_jeu.query(req).iloc[0]["cases"]
    if case_testee != "dispo" :
        print("Coup déjà joué")
        flag_coup_ok = False

    # teste si la case est voisine d'une case déjà jouée
    req = '(lig == ' + str(lig) + ' and col == ' + str(col - 1) + ' and cases != "dispo") or (lig == ' + str(lig) + ' and col == ' + str(col + 1) + ' and cases != "dispo") or (lig == ' + str(lig - 1) + ' and col == ' + str(col) + ' and cases != "dispo") or (lig == ' + str(lig + 1) + ' and col == ' + str(col) + ' and cases != "dispo")'
    df_jeu_cases_adj = df_jeu.query(req).iloc[:]["cases"].copy()
    if len(df_jeu_cases_adj) == 0:
        print("case non voisine d'une case jouée")
        flag_coup_ok = False

    # Teste si la case jouée permet de faire un sandwich
    

    return flag_coup_ok

#verifier_coup(echiquier, 3,4,"blanc")





