# Créez une classe “Personne” avec les attributs “nom” et “prenom”. Ajoutez une méthode
# “SePresenter()” qui retourne le nom et le prénom de la personne. Ajoutez aussi un
# constructeur prenant en paramètres de quoi donner des valeurs initiales aux attributs
# “nom” et “prenom”. Instanciez plusieurs personnes avec les valeurs de construction de
# votre choix et faites appel à la méthode “SePresenter()” afin de vérifier que tout
# fonctionne correctement.

class Personne:
    
    def __init__(self, nom, prenom):
      self.nom = nom 
      self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"
    
personne_1 = Personne("Doe", "John")
personne_2 = Personne("Dumont", "Lorrent")
personne_3 = Personne("Tuning", "Jackie")

print(personne_1.SePresenter())
print(personne_2.SePresenter())
print(personne_3.SePresenter())
    