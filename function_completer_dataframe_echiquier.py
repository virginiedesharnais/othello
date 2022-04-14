import pandas as pd
import numpy as np

def completer_dataframe_echiquier(df_echiquier, coup):
    """
    On a la dataframe du tour précédent, il faut ajouter la nouvelle intéraction qui peut être :
    
        * Le joueur a joué son pion sur une case vide

        * Un sandwitch transforme des pions déja placés

    D'où on on transforme le pion, quelquesoit sa position ou son type de case dans cette fonction.

    On entre en paramètre : coup, qui est une MODIFIABLE liste MODIFIABLE comprenant la ligne, colonne et la couleur.
    A cette ligne et colonne on transforme la case en la couleur annoncée.
    
    Ceci est bel et bien une fonction. On entre en argumant la dataframe et le coup et on return une dataframe.
    Donc on l'utilise de cette manière:

    df_echiquier = completer_dataframe_echiquier(df_echiquier, coup)
    """


    



