import pandas as pd
import numpy as np
import os

#les autres fichiers python sont dans ce même dossier othello, et VScode cherchera dans ce dossier ce qu'on cherche à importer
#import function_affichage_graphique    ne fonctionne pas comme tel; ou alors en notant function_affichage_graphique.affichage_graphique(_____)


from fonction_completer_df_coups import completer_df_coups  # fonction qui complète la liste des coups; ses paramètres : 
                # df_coups : DataFrame de la liste des coups à compléter
                # coup : DataFrame de la ligne qui a été jouée (à chercher avec querry)

from function_completer_dataframe_echiquier import completer_dataframe_echiquier  #fonction qui applique une modification sur la Dataframe,
                                                                                  # par posage ou sandwitch; ses paramètres :
            #df_echiquier : DataFrame de l'échiquier qu'on va changer
            #  coup : coup sous la forme d'une MODIFIABLE liste MODIFIABLE avec lig, col et cases en élément dans cet ordre.
                 
from function_affichage_graphique import (affichage_graphique, couleur)   # affichage graphique; de seul paramèter l'échiquier actuel



from function_fin_de_partie import fin_de_partie   # calcul le score une fois que la fin de partie a été annoncée, de paramètres :
                # df_echiquier : dataframe de l'échiquier à la fin de partie
                #  df_coups : dataframe des coups

from function_changement_couleur import changement_couleur # change "blanc" en "noir" et vice-versa



###On commence avec l'initialisation, validé dans partie_init. Les importations (de Seb) ont aussi été validés.
passe = False    #flag passe ton tour. 
passe_une_fois = False #flag de passe son tour une fois, qui se cumule avec le 1er pour annoncer une fin de partie.

fin_de_jeu = False   #flag de fin de partie
tour = 'noir'   #flag qui dit à qui de jouer. C'est aux noirs de débuter

ligne = list()
colonne = list()
for k in range(1, 9):
    for j in range(1, 9):
        ligne.append(k)
        colonne.append(j)

cases = ["dispo"]*64
cases[27] = "blanc"
cases[28] = "noir"
cases[35] = "noir"
cases[36] = "blanc"    #c'est l'installation de bases

dico = { "lig":ligne, "col":colonne, "cases":cases}
echiquier = pd.DataFrame(dico)
df_coups = pd.DataFrame( columns = echiquier.columns)
df_coups['numero']=[]

## On démarre
while fin_de_jeu == False and len(df_coups) < 64: #au cas où une sécurité
    print("C'est au tour du joueur {}.".format(tour))   #dit à quel joueur c'est de jouer
    
    action_valide = False
    
    while action_valide == False:
        action = str(input("'play' pour jouer une coordonnée.\n'pass' pour demander à passer ton tour :\n"))
        if action == 'play':
            
            ligne = int(input("Entrer le numéro de la ligne :"))
            colonne = int(input("Entrer le numéro de la colonne (a=1, b=2, c=3, d=4, e=5, f=6, g=7 et h=8) :"))
            
            #la couleur est déja donnée par "tour"
            #fonction virginnie

            if ??? == True: #si la fonction de Virginnie est applicable
                #obtenir la liste coup avec coordonnée ligne colonne couleur
                completer_dataframe_echiquier(echiquier, coup)

                completer_df_coups(df_coups, coup)  #attention au format des coups

                action_valide = True
            else: #si le programme de virginnie n'affiche pas que la coordonnée est invalide
                print('coordonnées invalide')


        elif action == 'pass':

            #fonction virginnie

            if ??? == True: #qu'on est effectivement obligé de passer le tour
                print("le tour est passé, c'est à maintenant à l'autre joueur.")

                passe = True

                action_valide = True

            else: #la fonction de virginnie a trouvé une possibilité de jouer
                #afficher la possibilité de jouer

        else: # ni play ni pass
            print("Veuillez saisir une action valide")

    affichage_graphique(echiquier)  #on affiche l'echiquier après le coup ou le non coup.
    tour = changement_couleur(tour)

    if passe_une_fois == True and passe == True: #si le joueur vient de passer son tour et le précédent aussi
        fin_de_jeu = True  
    elif passe == True:  #le joueur vient de passer son tour, mais le tour avant a été joué
        passe_une_fois = True
    else: # le tour vient d'être joué, quoiqu'il se soit passé le tour précédent
        passe = False
        passe_une_fois = False

#fin de partie
fin_de_partie(echiquier, df_coups)    


        
















