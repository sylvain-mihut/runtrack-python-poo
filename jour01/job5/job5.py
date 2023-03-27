# Créez une classe Animal avec un attribut age initialisé à zéro et prénom initialisé vide dans son constructeur.
# Instancier un objet Animal et écrire en console l’attribut âge. Créer une méthode “vieillir”
# qui ajoute 1 à l'âge de l’animal. Faire vieillir votre animal et afficher son âge en console.

class Animal:

    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom 
    
animal_1 = Animal()
animal_1.nommer("Cacahuete")
print(animal_1.prenom)
print(animal_1.age)
animal_1.vieillir()
print(animal_1.age)