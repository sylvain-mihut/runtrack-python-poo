# Créer une classe Personne qui aura comme attribut age prenant un entier et initialisé à
# 14 par défaut. Ajouter une méthode “afficherAge” qui affichera en console l’age de la
# personne et une méthode bonjour qui écrit en console ‘Hello’. Créer une méthode
# “modifierAge” prenant en paramètre un entier et permettant de modifier l’age de la personne.
# 
# Créer une classe Eleve qui hérite de la classe “Personne” qui n’a pas d’attribut et une
# méthode publique “allerEnCours” qui affiche : “Je vais en cours” ainsi qu’une méthode
# “affichageAge” qui écrit en console : ‘J’ai XX ans’
# Créer une classe Professeur avec un attribut privé “matiereEnseignée”, qui indiquera la
# matière du professeur, et une méthode publique “enseigner” qui affiche :. ‘Le cours va commencer’.
#
# Instancier une classe “Personne” et une classe “Eleve”. Afficher l’age par défaut de
# l’élève en console.

class Personne:
    def __init__(self):
       self.age = int(14)

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
       self.age = int(age)

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours():
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai : ", self.age, "ans")

class Professeur:
    def __init__(self, matiere):
        self.__matiereEnseignée = matiere
        
    def enseigner(self):
        print("le cours va commencer")


personne = Personne() 
eleve = Eleve()
eleve.affichageAge()