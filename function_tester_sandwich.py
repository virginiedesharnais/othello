import pandas as pd
import Partie_init as p_i

dic_dir = {"DHG":9, "DHD":7, "DBG":-7, "DBD":-9, "H":8, "B":-8, "D":-1, "G":1}

def est_sandwich(df_jeu, lig, col, case, direction) :
    l_sand_temp = list()
    l_sand = list()
    i =1
    flag_sand = False
    flag_autre_case = False
    pas = dic_dir[direction]
    pos_case = 8 * (lig-1) + col -1
    while (pos_case - pas * i > 0 and pos_case - pas * i<63 and (pos_case - pas * i)%8 != 0 and (pos_case - pas * i)%8 != 7) and flag_sand == False:
        if df_jeu.iloc[ pos_case - pas * i].values[2] != case and df_jeu.iloc[ pos_case - pas * i].values[2] != "dispo" :
            flag_autre_case = True
            l_sand_temp.append(pos_case - pas * i)
        if flag_autre_case == True and df_jeu.iloc[ pos_case - pas * i].values[2] == case :
            flag_sand = True
            l_sand=l_sand_temp.copy()
        i = i + 1
    
    return l_sand

def tester_sandwich(echiquier,lig,col,case) :
    for cle, valeur in dic_dir.items() :
        list_res = est_sandwich(echiquier,lig,col,case,cle)
        print("**** ",len(list_res))
        if len(list_res) != 0 :
            return True
            break
    return False

def renvoyer_sandwich(echiquier,lig,col,case) :
    list_sand_fin = list()
    for cle, valeur in dic_dir.items() :
        list_res = est_sandwich(echiquier,lig,col,case,cle)
        if len(list_res) != 0 :
            list_sand_fin = list_sand_fin + list_res
    return list_sand_fin

def tester_sandwich_possible(echiquier, case):
    flag_sand = False
    req = 'cases == "dispo"'
    list_jeu_cases_vides = echiquier.query('cases == "dispo"').index.values.tolist()
    for elem in list_jeu_cases_vides:
        s = echiquier.iloc[elem][["lig","col"]]
        if est_case_adj_contraire(echiquier,s[0],s[1],case) == True:
            if tester_sandwich(echiquier,s[0], s[1],case) == True:
                print(s[0], s[1],"=> sandwich possible")
                flag_sand = True
    return flag_sand

def est_case_adj_vide(df_jeu, lig, col):
    req = 'cases != "dispo" and ((lig == ' + str(lig -1) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig-1) + ' and col == ' + str(col +1) + ') or (lig == ' + str(lig+1 ) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig+1) + ' and col == ' + str(col + 1) + ') or (lig == ' + str(lig) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig) + ' and col == ' + str(col + 1) + ') or (lig == ' + str(lig - 1) + ' and col == ' + str(col) + ') or (lig == ' + str(lig + 1) + ' and col == ' + str(col) + '))'
    df_jeu_cases_adj = df_jeu.query(req).iloc[:]["cases"].copy()
    if len(df_jeu_cases_adj) == 0:
        return True
    else :
        return False

def est_case_adj_contraire(df_jeu, lig, col, case):
    req = 'cases != "' + case + '" and cases != "dispo" and ((lig == ' + str(lig -1) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig-1) + ' and col == ' + str(col +1) + ') or (lig == ' + str(lig+1 ) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig+1) + ' and col == ' + str(col + 1) + ') or (lig == ' + str(lig) + ' and col == ' + str(col - 1) + ') or (lig == ' + str(lig) + ' and col == ' + str(col + 1) + ') or (lig == ' + str(lig - 1) + ' and col == ' + str(col) + ') or (lig == ' + str(lig + 1) + ' and col == ' + str(col) + '))'
    df_jeu_cases_adj = df_jeu.query(req).iloc[:]["cases"].copy()
    if len(df_jeu_cases_adj) != 0:
        return True
    else :
        return False

# print(renvoyer_sandwich(p_i.echiquier,5,2,"blanc"))