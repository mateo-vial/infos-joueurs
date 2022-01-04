class Joueur:
    """
    Définition d'un joueur
    """

    _registry = []

    def __init__(self, drap = ['fr'], pseudo = None, prenom = None, twitter = None, fc = None, anniv = None, num = None, exteam = ['Aucune']):
        """
        Paramètres
        __________
        drap : list 
            list de strings correspondant aux id des pays, exemple drap=['fr', 'de']
        pseudo : string
            string contenant le pseudo du joueur, avec une majuscule, exemple emote='Gab'
        prenom : string
            string contenant le prénnom du joueur, avec majuscule, exemple prenom='Gabriel'
        twitter : string
            string contenant le pseudo twitter sans le @ au début, exemple twitter='sltcgabz'
        fc : string
            string contenant le FC du joueur (12 chiffres) sans séparateurs!!!, exemple fc='414930005733'
        anniv : string
            string contenant l'anniv du joueur (8 chiffres JJMMAAAA) sans séparateur, exemple anniv='10102000'
        num : string ou list
            string contenant le numéro de tel du joueur (10 chiffres) sans séparateur, exemple num='0652914850'
            si numéro étranger, faire une liste avec ['num', 'indicatif'], exemple : num=['0499343262', '32']
        exteam : list
            list de strings correspondant aux tags des anciennes teams dans l'ordre de préférence, exemple exteam=['мω', 'TP']
        """
        self._registry.append(self)
        self.drap = drap
        self.prenom = prenom
        if pseudo == None:
            self.pseudo = self.prenom
        else:
            self.pseudo = pseudo
        self.twitter = twitter
        self.fc = fc
        self.anniv = anniv # string
        self.annee = int(self.anniv[4:8])
        self.mois = int(self.anniv[2:4])
        self.jour = int(self.anniv[0:2])
        self.num = num
        self.exteam = exteam

    def affiche(self):
        """
        Renvoie le string correspondant à l'affiche complète du joueur
        """
        output = ''

        # écriture des drapeaux
        for drapeau in self.drap:
            output += ':flag_'+drapeau+': '
        
        # écriture pseudo et prénom
        if self.pseudo != self.prenom:
            output += self.pseudo+'/'
        output += self.prenom

        # écriture twitter
        if self.twitter != None:
            output += ', Twitter : ``@' + self.twitter+'``'

        output += '\n```'

        # écriture FC
        if self.fc != None:
            prefix = 'SW-'
            sep = '-'
            output += 'FC : '+ prefix + self.fc[0:4] + sep + self.fc[4:8] + sep + self.fc[8:12]
            output += '\n' 

        # écriture Anniv
        if self.anniv != None:
            sep = '/'
            output += 'Anniversaire : '
            output += self.anniv[0:2] + sep + self.anniv[2:4] + sep + self.anniv[4:8]
            output += '\n'

        # écriture Num
        if self.num != None:
            sep = ' '
            output += 'Num : '
            if type(self.num) == str:
                output += self.num[0:2] + sep + self.num[2:4] + sep + self.num[4:6] + sep + self.num[6:8] + sep + self.num[8:10]
            elif type(self.num) == list:
                output += self.num[0] + ' (+' + self.num[1] + ')'
            output += '\n'

        # écriture Ex-team
        sep = ', '
        output += 'Ex-team MK8D : '
        output += sep.join(self.exteam)

        # fin
        output += '```'
        return output