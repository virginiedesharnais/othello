import pandas as pd
import numpy as np

def couleur(col):
    """
    Si tu me dis que tu es "blanc", je te renvoie " B "
    Si tu me dis que tu es "noir",  je te renvoie " N "
                                      Sinon tu es " - "
    """
    if col == "noir":
        return " N "
    elif col == "blanc":
        return " B "
    else:
        return " - "


def affichage_graphique(df_echiquier):
    """
    Si on me donne le dataframe de l'echiquier, je ferai de mon mieux pour essayer de le print de manière précise.
    
    Cette DataFrame d'echiquier est une Dataframe de 64 lignes, avec 3 colonnes : "lig", "col" et "cases".
    lig et col servent à la localisation.
    Pour l'affichage graphique, je vais faire 9 print, avec donc les colonnes et les lignes et l'échiquier, avec B pour blanc, 
         N pour noir et - pour disponible.



    Je ne fais que print, je ne renvoie pas de valeur. Donc faite affichage_graphique(df_echiquier).
    """

    
    l0 = ["   ", " a "," b "," c "," d "," e "," f "," g "," h "]
    l1 = [" 1 "]
    l2 = [" 2 "]
    l3 = [" 3 "]
    l4 = [" 4 "]
    l5 = [" 5 "]
    l6 = [" 6 "]
    l7 = [" 7 "]
    l8 = [" 8 "]
    for c in range(8):
        #on va passer parles iloc de notre data frame pour ne pas galérer avec des querry. 
        #on prend les valeurs de la bonne igne, et la n°2 est bien celle de la colonne des cases, et on applique la fonction couleur
        l1.append(couleur(df_echiquier.iloc[ 8 * c + 0].values[2]))
        l2.append(couleur(df_echiquier.iloc[ 8 * c + 1].values[2]))
        l3.append(couleur(df_echiquier.iloc[ 8 * c + 2].values[2]))
        l4.append(couleur(df_echiquier.iloc[ 8 * c + 3].values[2]))
        l5.append(couleur(df_echiquier.iloc[ 8 * c + 4].values[2]))
        l6.append(couleur(df_echiquier.iloc[ 8 * c + 5].values[2]))
        l7.append(couleur(df_echiquier.iloc[ 8 * c + 6].values[2]))
        l8.append(couleur(df_echiquier.iloc[ 8 * c + 7].values[2]))




    
    print(l0)
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)




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

# affichage_graphique(echiquier)




