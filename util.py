def bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def jour_de_l_annee(annee, mois, jour):
    # Renvoie le numéro du jour dans l'année
    if not bissextile(annee):
        mois_taille = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    else:
        mois_taille = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    return mois_taille[mois-1] + jour