import pandas as pd
import numpy as np
import os      #va permettre de clear l'image à chaque fois qu'on fait l'affichage graphique plutôt que les cumuler

def couleur(coul):
    """
    Si tu me dis que tu es "blanc", je te renvoie " B  |"
    Si tu me dis que tu es "noir",  je te renvoie " N  |"
                                      Sinon tu es " -  |"
    """
    if coul == "noir":
        return " N  |"
    elif coul == "blanc":
        return " B  |"
    else:
        return " -  |"


def affichage_graphique(df_echiquier):
    """
    Si on me donne le dataframe de l'echiquier, je ferai de mon mieux pour essayer de le print de manière précise.
    
    Cette DataFrame d'echiquier est une Dataframe de 64 lignes, avec 3 colonnes : "lig", "col" et "cases".
    lig et col servent à la localisation.
    Pour l'affichage graphique, je vais faire 9 print, avec donc les colonnes et les lignes et l'échiquier, avec B pour blanc, 
         N pour noir et - pour disponible.



    Je ne fais que print, je ne renvoie pas de valeur. Donc faite affichage_graphique(df_echiquier).
    """

    os.system('clear')  #nettoie l'écran précédent

    l0 = ["    |", " a  |"," b  |"," c  |"," d  |"," e  |"," f  |"," g  |"," h  |"]
    l1 = [" 1  |"]
    l2 = [" 2  |"]
    l3 = [" 3  |"]
    l4 = [" 4  |"]
    l5 = [" 5  |"]
    l6 = [" 6  |"]
    l7 = [" 7  |"]
    l8 = [" 8  |"]
    for c in range(8):
        #on va passer parles iloc de notre data frame pour ne pas galérer avec des querry. 
        #on prend les valeurs de la bonne igne, et la n°2 est bien celle de la colonne des cases, et on applique la fonction couleur
        l1.append(couleur(df_echiquier.iloc[ 8 * 0 + c].values[2]))
        l2.append(couleur(df_echiquier.iloc[ 8 * 1 + c].values[2]))
        l3.append(couleur(df_echiquier.iloc[ 8 * 2 + c].values[2]))
        l4.append(couleur(df_echiquier.iloc[ 8 * 3 + c].values[2]))
        l5.append(couleur(df_echiquier.iloc[ 8 * 4 + c].values[2]))
        l6.append(couleur(df_echiquier.iloc[ 8 * 5 + c].values[2]))
        l7.append(couleur(df_echiquier.iloc[ 8 * 6 + c].values[2]))
        l8.append(couleur(df_echiquier.iloc[ 8 * 7 + c].values[2]))

    L0 = "".join(l0)
    L1 = "".join(l1)
    L2 = "".join(l2)
    L3 = "".join(l3)
    L4 = "".join(l4)
    L5 = "".join(l5)
    L6 = "".join(l6)
    L7 = "".join(l7)
    L8 = "".join(l8)

    
    print(L0+"\n---------------------------------------------")
    print(L1+"\n---------------------------------------------")
    print(L2+"\n---------------------------------------------")
    print(L3+"\n---------------------------------------------")
    print(L4+"\n---------------------------------------------")
    print(L5+"\n---------------------------------------------")
    print(L6+"\n---------------------------------------------")
    print(L7+"\n---------------------------------------------")
    print(L8+"\n---------------------------------------------")




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

# cases[9] = "noir"
# cases[10] = "noir"

# dico = { "lig":ligne, "col":colonne, "cases":cases}
# echiquier = pd.DataFrame(dico)

# affichage_graphique(echiquier)




