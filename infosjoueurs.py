import os

from listjoueurs import *

"""
Ecriture du fichier .txt
"""

nom_fichier = 'infosjoueurs.txt'

if os.path.isfile(nom_fichier):
    os.remove(nom_fichier)

f = open(nom_fichier, 'w+', encoding = 'utf-8')
f.write('\n'.join([joueur.affiche() for joueur in Joueur._registry]))