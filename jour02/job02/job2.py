# À l’aide de la classe “Personne” , Eleve et Professeur écrit au-dessus, faites dire bonjour
# à votre élève grâce à la méthode “bonjour” ainsi que “je vais en cours” grâce à la
# méthode “allerEnCours”. Redéfinir l’age de l’élève à 15 ans.
# Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le
# cours grâce à la méthode enseigner.

class Personne:
    def __init__(self):
       self.age = int(14)

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age) -> int:
       self.age = int(age)

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai : ", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiere):
        Personne.__init__(self)
        self.__matiereEnseignée = matiere
        
    def enseigner(self):
        print("le cours va commencer")

# personne = Personne()
eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.affichageAge()
professeur = Professeur("Math")
professeur.modifierAge(40)
professeur.bonjour()
professeur.enseigner()