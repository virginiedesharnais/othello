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

    * coup : dataframe d'une seule ligne, étant la ligne du dernier coup joué. Il contient donc la ligne, la colonne, et la couleur.

    Il nous suffira donc d'ajouter cette ligne à notre DataFrame et de compléter le numéro.

    Notre fonction renverra la DataFrame complété d'un coup. Donc pour l'appliquer ce sera :
    df_coups = completer_df_coups(df_coups, coup)
    """

    if len(df_coups) ==  0:
        #C'est à dire si c'est le 1er coups et que notre dataframe est vide.
        d = pd.DataFrame(df_coups)   #je passe toujours par des copies MOI
        ### Je vais passer par des array afin de pouvoir prélever les valeurs, car les colonnes de coup sont des séries d'un 
           # d'un seul élément
        ligne = coup['lig'].values
        colonne = coup['col'].values
        case = coup['cases'].values

        d.iloc[0] = [ligne[0], colonne[0], case[0], 1]   #on complète avec les coordonnées du coup, + le numéro qui est le 1er coup

    else: #donc ce n'est pas le premier coup

        d = pd.DataFrame(df_coups)
        ligne = coup['lig'].values
        colonne = coup['col'].values
        case = coup['cases'].values
        num = len(df_coups) + 1

        d.iloc[num] = [ligne[0], colonne[0], case[0], num]

    return d


    





