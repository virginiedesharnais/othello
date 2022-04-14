import pandas as pd
import numpy as np

def fin_de_partie(df_echiquier, df_coups):
    """
    Cette fonction est acctivé lorsque la partie est finie.
    Elle prend en entrée :
    * La Dataframe actuelle pour le calcul des scores
    * La Dataframe des coups qu'elle affiche (on peut ajouter une option qui demande si on veut l'afficher)

    Cette fonction :
    * affichera la dataframe des coups joués.
    * affichera la couleur gagnante ainsi que les scores avec un splendide texte.

    """

    score= df_echiquier['cases'].value_counts()   
    # le vainqueur sera score.index[0] car quand la partie finie généralement il n'y a pas beaucoup de vides.
    print("Commençons par la liste des coups :")
    print(df_coups)
    print("Et maintenant les scores !!!!!!!")
    print(score)
    print("Notre grand vainqueur est bel est bien le joueur incarnant les {}, bravo à lui !".format(score.index[0]))
    print("Une pensée pour le deuxième joueur ...")
    
    





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
# df_coups = pd.DataFrame( columns = echiquier.columns)
# df_coups['numero']=[]
# df_coups.loc[0] = [ 2, 3, "noir", 1]

# fin_de_partie(echiquier, df_coups)