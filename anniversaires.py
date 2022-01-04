import os

from listjoueurs import *
from util import jour_de_l_annee

"""
Liste des mois temporaires pour ensuite instancer des classes
"""

liste_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

"""
Créatiion de la classe et des instances
"""

class Mois:
    def __init__(self, val): # val est le numéro du mois de 1 à 12 comme renseigné dans la classe Joueurs.
        self.nom = liste_mois[val-1]
        self.val = val
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)
    
mois_instances = []
for i in range(1,13):
    mois_instances.append(Mois(val = i))

"""
Remplissage des instances de Joueurs dans l'attribut liste_joueurs des instances de Mois
"""

for m in mois_instances:
    for joueur in Joueur._registry:
        if joueur.mois == m.val:
            m.ajouter_joueur(joueur)
    m.joueurs.sort(key = lambda joueur: joueur.jour) 

"""
Ecriture du fichier anniversaires.txt
"""

nom_fichier = 'anniversaires.txt'

max_lettres = max([len(mois) for mois in liste_mois])

if os.path.isfile(nom_fichier):
    os.remove(nom_fichier)

f = open(nom_fichier, 'w+', encoding = 'utf-8')
f.write(':birthday: Anniversaires\n```')

sep = ', '
for mois in mois_instances:
    f.write((' ' * (max_lettres - len(mois.nom))) + mois.nom + ' : ' + sep.join([joueur.pseudo + ' (' + str(joueur.jour) + ')' for joueur in mois.joueurs]) + '\n')

f.write('```')