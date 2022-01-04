from listjoueurs import *
from util import jour_de_l_annee
import os

"""
Ce programme génère deux fichiers 'naissance.txt' et 'anniversaires.txt' 

Le premier fichier contient la liste des joueurs classés par naissance et par année (avec possibilité d'afficher ou non les dates d'anniversaires précises)

Le deuxième fichier contient la liste des joueurs classés par ordre d'anniversaire dans l'année et par mois avec le numéro du jour affiché
"""

"""
Créer une liste temporaire contenant chaque année de naissance des joueurs une seule fois et triée
"""

annees = []

for joueur in Joueur._registry:
    if joueur.annee not in annees:
        annees.append(joueur.annee)

nbannees = len(annees)

annees.sort()

"""
Définir la classe Année
"""

class Annee:
    def __init__(self, val):
        self.val = val # valeur de l'année (int)
        self.joueurs = [] # Liste contenant les instances des joueurs nés à l'année self.val
    
    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur) # Ajouter une instance joueur à la liste self.joueurs

"""
Créer une instance Année pour chaque valeur de la liste annees. 
"""

annees_instances = []
for i in annees:
    annees_instances.append(Annee(val = i))

"""
Ajouter les (instances) joueurs pour chaque année et les trier par le critère jour_de_l_annee
"""

for a in annees_instances:
    for joueur in Joueur._registry:
        if joueur.annee == a.val:
            a.ajouter_joueur(joueur)
    # l'année a est bien complétée, maintenant on trie a.joueurs
    a.joueurs.sort(key = lambda joueur: jour_de_l_annee(joueur.annee, joueur.mois, joueur.jour))
# toutes les années sont complétées et triées

"""
Ecrire le fichier naissances.txt
"""

affiche_jours = 'PLACEHOLDER'
while affiche_jours not in ['y', 'n', '']:
    affiche_jours = input('Afficher les jours ? [y]/n ')
if affiche_jours == '':
    affiche_jour = 'y'

nom_fichier = 'naissances.txt'

if os.path.isfile(nom_fichier):
    os.remove(nom_fichier)

f = open(nom_fichier, 'w+', encoding = 'utf-8')
f.write(':baby: Naissances\n```')

sep = ' > '
for a in annees_instances:
    f.write(str(a.val) + ' : ' + sep.join([joueur.pseudo + (affiche_jours == 'y') * (' (' + str('{:02d}'.format(joueur.jour)) + '/' + str('{:02d}'.format(joueur.mois)) + ')') for joueur in a.joueurs]) + '\n')

f.write('```')