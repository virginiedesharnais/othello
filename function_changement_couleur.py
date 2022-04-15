
def changement_couleur(coul):
    """
    Si la couleur est "noir", on renvoie "blanc" 
    Si la couleur est "blanc", on renvoie "noir"
    On l'applique ave cun return, c'est à dire :
    tour = changement_couleur(tour)
    """
    if coul == "noir":
        return "blanc"
    elif coul == "blanc":
        return "noir"

    else:
        print("erreur de saisie de couleur")

# tour = "noir"
# print("On commence noir : ", tour)
# tour = changement_couleur(tour)
# print("on applique une fois :", tour)
# tour = changement_couleur(tour)
# print("Une deuxième fois :", tour)

# print("Et si on fait n'importe quoi !", changement_couleur('banane'))