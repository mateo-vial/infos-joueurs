from classjoueur import Joueur

# Modèle : Pseudo = Joueur(drap = [], pseudo = '', prenom = '', twitter = '', fc = '', anniv = '', num = '', exteam = [])
# ne pas mettre si non spécifié (num et exteam en particulier)
# ne pas mettre pseudo si pseudo=prénom
# vérifier dans classjoueur.py pour plus d'infos sur les paramètres

"""
Définition des joueurs
"""

Joueur1 = Joueur(drap = ['fr'], pseudo = 'MaxBG', prenom = 'Jean-Michel', twitter = 'twittertest', fc = '123412341234', anniv = '01012000', num = '0606060606', exteam = ['team1', 'team2'])
Joueur2 = Joueur(drap = ['fr', 'be'], pseudo = 'pseudonul', prenom = 'Luc', twitter = 'lucbg', fc = '123412340000', anniv = '01022003')
