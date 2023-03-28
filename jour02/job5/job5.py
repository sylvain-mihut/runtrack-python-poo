# Récupérer votre classe “Forme” crée juste au-dessus.
# Créer une classe fille nommée “Cercle” qui hérite de la classe “Forme” et possédant un
# attribut radius.
# Surcharger la méthode “aire” dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les
# différentes surcharges de la méthode aire en affichant les résultats en console.

class Forme:
    def __init__(self):
       pass

    def Aire(self):
        self.aire = 0
        return self.aire
    
class Rectangle(Forme):
    def __init__(self):
        Forme.__init__(self)
        self.hauteur = 10
        self.largueur = 5

    def Aire(self):
        self.aire = self.hauteur * self.largueur
        return self.aire 

class Cercle(Forme):
    def __init__(self):
        Forme.__init__(self)
        self.radius = 5

    def Aire(self):
        self.aire = (self.radius*self.radius) * 3.14
        return self.aire

cercle = Cercle()
rectangle = Rectangle()

print(rectangle.Aire())
print(cercle.Aire())