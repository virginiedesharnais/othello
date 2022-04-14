import pandas

dic_dir = {"DHG":9, "DHD":7, "DBG":-7, "DBD":-9, "H":8, "B":-8, "D":-1, "G":1}

def est_sandwich(df_jeu, lig, col, case, direction) :
    i =1
    flag_sand = False
    pas = dic_dir[direction]
    pos_case = 8 * (lig-1) + col -1
    while ((pos_case - pas * i)%8 != 0 and (pos_case - pas * i)%8 != 7) and flag_sand == False:
        if df_jeu.iloc[ pos_case - pas * i].values[2] == case :
            flag_sand = True
        i = i + 1
    
    return flag_sand

def tester_sandwich(echiquier,lig,col,case) :
    for cle, valeur in dic_dir.items() :
        res = est_sandwich(echiquier,lig,col,case,cle)
        if res == True :
            return True
            break
    return False

