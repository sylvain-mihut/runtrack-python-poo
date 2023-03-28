# Créer une classe nommée “Forme” possédant une méthode nommée aire qui renvoie 0.
# Créer une classe “Rectangle” qui hérite de la classe “Forme” et qui possède deux
# attributs largeur et hauteur. Surcharger la méthode aire dans la classe Rectangle afin
# qu’elle ne renvoie plus 0, mais l’aire du rectangle.
# Imprimer en console le résultat de la méthode aire de la classe Rectangle.

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
    

rectangle = Rectangle()

print(rectangle.Aire())