
#On initialise le début de partie.
passe = False    #flag passe ton tour. 

import pandas as pd
index = range(64) #ce sera l'index de notre DataFrame
ligne = list()
colonne = list()
for k in range(1, 9):
    for j in range(1, 9):
        ligne.append(k)
        colonne.append(j)

#ligne est donc [1,1,1,1,1,1,1,1,2,2,2,2,....] et colonne [1,2,3,4,5,6,7,8,1,2,3, ...] de tailles 64

cases = ["dispo"]*64
cases[27] = "blanc"
cases[28] = "noir"
cases[35] = "noir"
cases[36] = "blanc"    #c'est l'installation de bases

# print(cases, "\n", ligne, "\n", colonne)

dico = { "lig":ligne, "col":colonne, "cases":cases}
echiquier = pd.DataFrame(dico)
# print(echiquier.head(40))

liste_coups = pd.DataFrame( columns = echiquier.columns)
liste_coups['numero']=[]
# print(liste_coups)







