import pandas as pd
import numpy as np

def completer_df_coups(df_coups, coup):
    """
    On met en argumant la liste des coups précédents qui sera complété : une DataFrame (étant vide au tout 1er coup), de colonne :
    lig
    col
    case
    numero

    et qui completera par le dernier coup joué grâce aux arguments :

    * coup : liste de troius éléments dans cet ordre:  la ligne, la colonne, et la couleur.

    Il nous suffira donc d'ajouter cette ligne à notre DataFrame et de compléter le numéro.

    Notre fonction renverra la DataFrame complété d'un coup. Donc pour l'appliquer ce sera :
    df_coups = completer_df_coups(df_coups, coup)
    """


    d = pd.DataFrame(df_coups)
    ### Je vais passer par des array afin de pouvoir prélever les valeurs, car les colonnes de coup sont des séries d'un 
       # d'un seul élément   
    ligne = coup[0]
    colonne = coup[1]
    case = coup[2]
    num = len(df_coups) 

    d.loc[num + 1] = [ligne, colonne, case, num + 1]

    return d


# ligne = list()
# colonne = list()
# for k in range(1, 9):
#     for j in range(1, 9):
#         ligne.append(k)
#         colonne.append(j)
# cases = ["dispo"]*64
# cases[27] = "blanc"
# cases[28] = "noir"
# cases[35] = "noir"
# cases[36] = "blanc"

# dico = { "lig":ligne, "col":colonne, "cases":cases}
# echiquier = pd.DataFrame(dico)    
# df_coups = pd.DataFrame( columns = echiquier.columns)
# df_coups['numero']=[]


# dico2 = { "lig":[2], "col":[4], "cases":["noir"]}
# coup = pd.DataFrame(dico2)

# df_coups = completer_df_coups(df_coups, coup)
# print(df_coups)

