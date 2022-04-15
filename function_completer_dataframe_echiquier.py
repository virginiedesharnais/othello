import pandas as pd
import numpy as np

def completer_dataframe_echiquier(df_echiquier, coup):
    """
    On a la dataframe du tour précédent, il faut ajouter la nouvelle intéraction qui peut être :
    
        * Le joueur a joué son pion sur une case vide

        * Un sandwitch transforme des pions déja placés

    D'où on on transforme le pion, quelquesoit sa position ou son type de case dans cette fonction.

    On entre en paramètre : coup, qui est une liste comprenant la ligne, colonne et la couleur dans cet ordre.
    A cette ligne et colonne on transforme la case en la couleur annoncée.
    
    Ceci est bel et bien une fonction. On entre en argumant la dataframe et le coup et on return une dataframe.
    Donc on l'utilise de cette manière:

    df_echiquier = completer_dataframe_echiquier(df_echiquier, coup)
    """


    #coup est donc le forme [n° ligne, n° colonne, couleur]
    # puisqu'on est assez malin, on va calculer l'index de la dataframe avec iloc plutôt que querry et chercher les index et galérer
    # l'index de iloc est 8 x (n°ligne - 1) + n°colonne - 1  ; le dernier -1 car iloc part de 0

    d = pd.DataFrame(df_echiquier) #passer par des copies
    d.iloc[8 * (coup[0] - 1) + coup[1] - 1] = [ coup[0], coup[1], coup[2]] 

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

# coup = [3, 4, "noir"] #correspond à l'index 19 
# print(completer_dataframe_echiquier(echiquier, coup).head(30))


